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
  --acc:#10b981;
  --user:#ecfeff;
  --bot:#fff7ed;
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

# ── 세션 상태 ────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ── OpenAI 클라이언트 ────────────────────────────────────────────────────────
def get_client() -> Optional[OpenAI]:
    if api_key_input and api_key_input.strip():
        st.session_state["OPENAI_API_KEY"] = api_key_input.strip()

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
    if hasattr(st, "write_stream"):
        return st.write_stream(gen)
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

# ── 키 안내 ───────────────────────────────────────────────────────────────────
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하면 세션에 저장되어 계속 사용됩니다.", icon="🔐")

# ── 자유 채팅 입력(하단 고정) ────────────────────────────────────────────────
user_input = st.chat_input("메시지를 입력하세요…")

if user_input and client:
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})
    history.extend(st.session_state.messages)
    user_msg = {"role": "user", "content": user_input}
    history.append(user_msg)

    render_message("user", user_input)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    with st.chat_message("assistant", avatar="🤖"):
        try:
            response_text = write_stream_safe(
                stream_completion_text(client, history, model, temperature, max_tokens)
            )
        except openai.AuthenticationError:
            st.error("**인증 오류(401)**: API Key가 잘못되었거나 만료되었습니다.", icon="🚫"); st.stop()
        except openai.PermissionDeniedError:
            st.error("**권한 오류(403)**: 선택한 모델 권한 없음.", icon="🔒"); st.stop()
        except openai.RateLimitError:
            st.warning("**요청 제한(429)**: 잠시 후 재시도.", icon="⏳"); st.stop()
        except openai.BadRequestError as e:
            st.error(f"**요청 오류(400)**: {e}", icon="❗"); st.stop()
        except openai.OpenAIError as e:
            st.error(f"OpenAI 오류: {e}", icon="💥"); st.stop()

    st.session_state.messages.append(
        {"role": "assistant", "content": response_text or "(응답 없음)", "time": datetime.now().strftime("%H:%M")}
    )

# ── 메인 프롬프트 박스(텍스트 + 액션 버튼) ───────────────────────────────────
st.markdown("<hr/>", unsafe_allow_html=True)
with st.container():
    st.markdown("#### 프롬프트")
    main_text = st.text_area(
        "여기에 텍스트를 붙여넣고 요약/번역/리뷰 버튼을 누르세요.",
        key="__main_task_area",
        height=160,
        label_visibility="collapsed",
        placeholder="텍스트를 입력하거나 붙여넣기…"
    )
    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None
    if c1.button("요약(3줄)", use_container_width=True, key="main_sum"):
        send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + (main_text or "")
    if c2.button("영→한 번역", use_container_width=True, key="main_tr"):
        send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + (main_text or "")
    if c3.button("코드 리뷰", use_container_width=True, key="main_rev"):
        send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + (main_text or "")
    if c4.button("그대로 보내기", use_container_width=True, key="main_send"):
        send_prompt = main_text or ""

# 커스텀 박스에서 눌렀다면 즉시 전송(대화 히스토리에 추가)
if send_prompt and client:
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})
    history.extend(st.session_state.messages)
    user_msg = {"role": "user", "content": send_prompt}
    history.append(user_msg)

    render_message("user", send_prompt)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    with st.chat_message("assistant", avatar="🤖"):
        try:
            response_text = write_stream_safe(
                stream_completion_text(client, history, model, temperature, max_tokens)
            )
        except openai.AuthenticationError:
            st.error("**인증 오류(401)**: API Key가 잘못되었거나 만료되었습니다.", icon="🚫"); st.stop()
        except openai.PermissionDeniedError:
            st.error("**권한 오류(403)**: 선택한 모델 권한 없음.", icon="🔒"); st.stop()
        except openai.RateLimitError:
            st.warning("**요청 제한(429)**: 잠시 후 재시도.", icon="⏳"); st.stop()
        except openai.BadRequestError as e:
            st.error(f"**요청 오류(400)**: {e}", icon="❗"); st.stop()
        except openai.OpenAIError as e:
            st.error(f"OpenAI 오류: {e}", icon="💥"); st.stop()

    st.session_state.messages.append(
        {"role": "assistant", "content": response_text or "(응답 없음)", "time": datetime.now().strftime("%H:%M")}
    )
    st.rerun()

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

# ── 빌드 태그 ─────────────────────────────────────────────────────────────────
st.markdown("<hr/>", unsafe_allow_html=True)
st.caption("build: streamlit_app.py · layout=wide · light theme")
