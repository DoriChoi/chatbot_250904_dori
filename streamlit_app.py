# streamlit_app.py
from __future__ import annotations
import json
from datetime import datetime
from typing import Dict, List, Generator, Optional

import streamlit as st
import openai
from openai import OpenAI

# ── 페이지 설정 ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 라이트 & 상큼한 컬러 CSS ───────────────────────────────────────────────────
st.markdown("""
<style>
:root{
  --bg:#ffffff;
  --card:#ffffff;
  --acc:#10b981;            /* 민트 포인트 */
  --user:#ecfeff;           /* 연한 민트 말풍선 */
  --bot:#fff7ed;            /* 연한 피치 말풍선 */
  --text:#111827;
  --muted:#6b7280;
  --border:#e5e7eb;
}
html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(1200px 800px at 10% 10%, #f0f9ff 0%, var(--bg) 70%) !important;
  color: var(--text) !important;
}
section[data-testid="stSidebar"]{
  background-color: var(--card) !important;
  border-right: 1px solid var(--border);
}
.block-container{padding-top: 1.0rem;}
div.stTextInput>div>div>input, textarea, .stSelectbox [data-baseweb="select"]{
  background-color:#ffffff !important; color:var(--text) !important; border:1px solid var(--border) !important;
}
.stButton>button{
  background: linear-gradient(90deg, #34d399, #10b981);
  border:0; color:white; font-weight:700;
  box-shadow: 0 4px 14px rgba(16,185,129,.25);
}
.stButton>button:hover{filter:brightness(1.04);}
.chat-header{
  border:1px solid var(--border);
  background: linear-gradient(90deg, #f0fdf4, #ecfeff 60%, #f0f9ff);
  padding:16px 20px; border-radius:14px;
  box-shadow: 0 8px 24px rgba(2,132,199,.12);
}
.msg{border:1px solid var(--border); padding:14px 16px; border-radius:14px; margin:8px 0; line-height:1.55;}
.msg.user{background-color: var(--user);}
.msg.bot{background-color: var(--bot);}
.msg .meta{font-size:12px; color:var(--muted); margin-bottom:6px;}
hr{border-color:var(--border);}
small.hint{color:var(--muted);}
kbd{background:#f8fafc; border:1px solid var(--border); border-bottom-width:2px; padding:1px 6px; border-radius:6px;}
</style>
""", unsafe_allow_html=True)

# ── 상단 헤더 ─────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="chat-header">
      <h2 style="margin:0;">💬 Chatbot</h2>
      <div style="color:#6b7280;margin-top:6px;">
        OpenAI Chat API 기반. 좌측에서 <b>모델/온도/시스템프롬프트</b>를 조절하세요.
        <b>API Key는 입력창에 넣으면 세션에 저장</b>됩니다(Secrets 불필요).
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ── 사이드바(설정/유틸) ───────────────────────────────────────────────────────
with st.sidebar:
    st.subheader("환경 설정")

    # 세션에 이미 저장된 키가 있으면 그걸 기본값으로 사용 (Secrets 의존 X)
    key_default = st.session_state.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input(
        "OpenAI API Key",
        value=key_default,
        type="password",
        help="입력하면 세션에 저장됩니다. 새 세션/새 탭에선 다시 입력 필요."
    )

    model = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini", "gpt-3.5-turbo"],
        index=0
    )
    temperature = st.slider("Temperature", 0.0, 1.2, 0.7, 0.1)
    max_tokens = st.slider("Max tokens(응답)", 256, 4096, 1024, 64)

    system_prompt = st.text_area(
        "System prompt",
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 **굵게** 강조합니다.",
        height=100
    )

    st.divider()
    col_a, col_b = st.columns(2)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True)
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True)

    # ── 추천 작업(텍스트 + 액션 버튼) ────────────────────────────────────────
    st.markdown("#### 추천 질문")
    examples_toggle = st.toggle("패널 열기", value=False)
    if examples_toggle:
        st.caption("여기에 작업할 텍스트를 붙여넣고, 아래 버튼을 누르세요.")
        task_text = st.text_area("작업 대상 텍스트", key="__task_text_area", height=140)

        c1, c2, c3 = st.columns(3)
        if c1.button("요약(3줄)", use_container_width=True, key="sug_sum"):
            st.session_state["__suggestion"] = "아래 텍스트를 3줄로 요약해줘:\n\n"
            st.session_state["__task_text"] = task_text or ""
        if c2.button("영→한 번역", use_container_width=True, key="sug_tr"):
            st.session_state["__suggestion"] = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n"
            st.session_state["__task_text"] = task_text or ""
        if c3.button("코드 리뷰", use_container_width=True, key="sug_rev"):
            st.session_state["__suggestion"] = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n"
            st.session_state["__task_text"] = task_text or ""
    else:
        st.session_state.pop("__suggestion", None)
        st.session_state.pop("__task_text", None)

# ── 세션 상태 ────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ── OpenAI 클라이언트 ────────────────────────────────────────────────────────
def get_client() -> Optional[OpenAI]:
    # 1) 방금 입력값이 있으면 세션에 반영
    if api_key_input and api_key_input.strip():
        st.session_state["OPENAI_API_KEY"] = api_key_input.strip()

    # 2) 세션에 있는 키 사용
    key = st.session_state.get("OPENAI_API_KEY", "").strip()
    if not key:
        return None

    try:
        return OpenAI(api_key=key)
    except openai.OpenAIError as e:
        st.error(f"OpenAI 클라이언트 초기화 실패: {e}", icon="💥")
        return None

client = get_client()

# ── 스트리밍(문자열 제너레이터) ───────────────────────────────────────────────
def stream_completion_text(
    _client: OpenAI,
    _messages: List[Dict[str, str]],
    _model: str,
    _temperature: float,
    _max_tokens: int,
) -> Generator[str, None, None]:
    """
    chat.completions 스트림에서 delta.content를 문자열로 yield.
    st.write_stream에 넣으면 단일 요소에 타자 효과로 출력됨.
    """
    resp = _client.chat.completions.create(
        model=_model,
        messages=_messages,
        temperature=_temperature,
        max_tokens=_max_tokens,
        stream=True,
    )
    for chunk in resp:
        if chunk.choices and getattr(chunk.choices[0].delta, "content", None):
            yield chunk.choices[0].delta.content

def write_stream_safe(gen: Generator[str, None, None]) -> str:
    """
    Streamlit 버전에 따라 st.write_stream 유무가 다를 수 있어
    안전하게 처리. 없으면 placeholder로 직접 스트리밍.
    """
    if hasattr(st, "write_stream"):
        return st.write_stream(gen)  # 최종 문자열 반환
    # fallback
    ph = st.empty()
    acc = []
    for tok in gen:
        acc.append(tok)
        ph.markdown(
            f'<div class="msg bot"><div class="meta">assistant · {datetime.now():%H:%M}</div>'
            f'{"".join(acc)}</div>',
            unsafe_allow_html=True
        )
    return "".join(acc)

# ── 기존 메시지 렌더링 ────────────────────────────────────────────────────────
def render_message(role: str, content: str, when: Optional[str] = None):
    meta = when or datetime.now().strftime("%H:%M")
    with st.chat_message("assistant" if role == "assistant" else "user",
                         avatar="🤖" if role == "assistant" else "🧑"):
        st.markdown(
            f'<div class="msg {"bot" if role=="assistant" else "user"}">'
            f'<div class="meta">{role} · {meta}</div>{content}</div>',
            unsafe_allow_html=True
        )

for m in st.session_state.messages:
    render_message(m["role"], m["content"], m.get("time"))

# ── 추천 작업 값 한 번만 소비 ────────────────────────────────────────────────
suggestion: Optional[str] = st.session_state.pop("__suggestion", None)
task_text_mem: Optional[str] = st.session_state.pop("__task_text", None)

# suggestion이 있으면 chat_input 대신 즉시 전송용 prompt 구성
if suggestion:
    combined = suggestion + (task_text_mem or "")
else:
    combined = None

# ── 키 안내 ───────────────────────────────────────────────────────────────────
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하면 세션에 저장되어 계속 사용됩니다.", icon="🔐")

# ── 채팅 입력 ────────────────────────────────────────────────────────────────
user_input = None if combined else st.chat_input("메시지를 입력하세요…")
final_prompt = combined or user_input

if final_prompt and client:
    # 1) 메시지 스택 구성
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})
    history.extend(st.session_state.messages)
    user_msg = {"role": "user", "content": final_prompt}
    history.append(user_msg)

    # 2) 사용자 메시지 출력 + 세션 기록
    render_message("user", final_prompt)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    # 3) 어시스턴트 스트리밍 (예외 처리 포함)
    with st.chat_message("assistant", avatar="🤖"):
        try:
            response_text = write_stream_safe(
                stream_completion_text(client, history, model, temperature, max_tokens)
            )
        except openai.AuthenticationError:
            st.error("**인증 오류(401)**: API Key가 잘못되었거나 만료되었습니다. 사이드바에 올바른 키를 다시 입력하세요.", icon="🚫")
            st.stop()
        except openai.PermissionDeniedError:
            st.error("**권한 오류(403)**: 선택한 모델에 대한 권한이 없습니다. 모델을 변경하거나 계정을 확인하세요.", icon="🔒")
            st.stop()
        except openai.RateLimitError:
            st.warning("**요청 제한(429)**: 호출이 많거나 한도를 초과했습니다. 잠시 후 다시 시도하세요.", icon="⏳")
            st.stop()
        except openai.BadRequestError as e:
            st.error(f"**요청 오류(400)**: 파라미터/모델명이 잘못되었을 수 있습니다. 상세: {e}", icon="❗")
            st.stop()
        except openai.OpenAIError as e:
            st.error(f"OpenAI 오류: {e}", icon="💥")
            st.stop()

    st.session_state.messages.append(
        {"role": "assistant", "content": response_text or "(응답 없음)", "time": datetime.now().strftime("%H:%M")}
    )

# ── 내려받기 ───────────────────────────────────────────────────────────────────
if download_clicked:
    fname = f"chat_{datetime.now():%Y%m%d_%H%M%S}.json"
    st.download_button(
        "대화 내용 저장",
        data=json.dumps(st.session_state.messages, ensure_ascii=False, indent=2),
        file_name=fname,
        mime="application/json",
        use_container_width=True
    )
    st.caption("대화 기록을 JSON으로 저장했습니다.")

# ── 빌드 태그(배포 반영 확인용) ────────────────────────────────────────────────
st.markdown("<hr/>", unsafe_allow_html=True)
st.caption("build: streamlit_app.py · layout=wide · light theme")
