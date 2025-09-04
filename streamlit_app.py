# streamlit_app.py
from __future__ import annotations
import json
from datetime import datetime
from typing import Dict, List, Generator

import streamlit as st
from openai import OpenAI

# ───────────── 페이지 기본 설정 (앱 최상단에서 1회만) ─────────────
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ───────────── 라이트 & 상큼한 컬러 CSS 주입 ─────────────
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

# ───────────── 상단 헤더 ─────────────
st.markdown(
    """
    <div class="chat-header">
      <h2 style="margin:0;">💬 Chatbot</h2>
      <div style="color:#6b7280;margin-top:6px;">
        OpenAI Chat API 기반. 좌측에서 <b>모델/온도/시스템프롬프트</b>를 조절하고, API Key는 secrets 또는 입력으로 설정하세요.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ───────────── 사이드바: 설정 & 유틸 ─────────────
with st.sidebar:
    st.subheader("환경 설정")
    # 우선순위: secrets → 입력
    default_key = st.secrets.get("OPENAI_API_KEY", "")
    api_key = st.text_input("OpenAI API Key", value=default_key, type="password",
                            help="배포에선 Cloud의 Secrets 탭 권장. 로컬은 .streamlit/secrets.toml 사용 가능.")

    model = st.selectbox(
        "Model",
        options=[
            "gpt-4o-mini",
            "gpt-4o",
            "gpt-4.1-mini",
            "gpt-3.5-turbo"
        ],
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
    col_a, col_b, col_c = st.columns(3)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True)
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True)
    examples_toggle = col_c.toggle("추천 질문", value=False)

# ───────────── 세션 상태 ─────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ───────────── OpenAI 클라이언트 ─────────────
def get_client() -> OpenAI | None:
    k = (api_key or "").strip()
    if not k:
        return None
    return OpenAI(api_key=k)

client = get_client()

# ───────────── 스트리밍(문자열 제너레이터) ─────────────
def stream_completion_text(
    _client: OpenAI,
    _messages: List[Dict[str, str]],
    _model: str,
    _temperature: float,
    _max_tokens: int,
) -> Generator[str, None, None]:
    """
    chat.completions.create(stream=True)로 받은 토큰을 문자열만 yield.
    Streamlit의 st.write_stream이 단일 요소에 '타자 효과'로 출력한다.
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
            yield chunk.choices[0].delta.content  # 문자열만 넘긴다

# ───────────── 기존 메시지 렌더 ─────────────
def render_message(role: str, content: str, when: str | None = None):
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

# ───────────── 추천 질문 (옵션) ─────────────
if examples_toggle:
    st.caption("클릭하면 입력창에 채워집니다.")
    c1, c2, c3 = st.columns(3)
    if c1.button("요약해줘(3줄)", use_container_width=True):
        st.session_state._chat_input = "아래 텍스트를 3줄로 요약해줘:\n\n"
    if c2.button("영→한 번역", use_container_width=True):
        st.session_state._chat_input = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n"
    if c3.button("코드 리뷰", use_container_width=True):
        st.session_state._chat_input = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n"

# ───────────── 키 안내 ─────────────
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하세요. 배포에선 Cloud의 **Secrets**에 저장 후 `st.secrets`로 읽는 것이 안전합니다.", icon="🔐")

# ───────────── 채팅 입력 ─────────────
# (추천 질문 버튼으로 채워준 값이 있으면 기본값으로 사용)
default_prompt = st.session_state.pop("_chat_input", None) if "_chat_input" in st.session_state else None
prompt = st.chat_input("메시지를 입력하세요…", default=default_prompt)

if prompt and client:
    # 1) 메시지 스택 구성 (system → history → user)
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})
    history.extend(st.session_state.messages)
    user_msg = {"role": "user", "content": prompt}
    history.append(user_msg)

    # 2) 화면에 유저 메시지 먼저 표시 + 세션 기록
    render_message("user", prompt)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    # 3) 어시스턴트 스트리밍 (중복 없이 단일 요소로)
    with st.chat_message("assistant", avatar="🤖"):
        response_text = st.write_stream(
            stream_completion_text(client, history, model, temperature, max_tokens)
        )
    st.session_state.messages.append(
        {"role": "assistant", "content": response_text or "(응답 없음)", "time": datetime.now().strftime("%H:%M")}
    )

# ───────────── 내려받기 ─────────────
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

# ───────────── 빌드 태그(배포 반영 확인용) ─────────────
st.markdown("<hr/>", unsafe_allow_html=True)
st.caption("build: streamlit_app.py · layout=wide · light theme")
