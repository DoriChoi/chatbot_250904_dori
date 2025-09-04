# app_chat_pretty.py
import json
from datetime import datetime
from typing import Generator, List, Dict

import streamlit as st
from openai import OpenAI

# ---------- 페이지 기본 설정 ----------
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- CSS: 색/말풍선/헤더 ----------
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

# ---------- 상단 헤더 ----------
with st.container():
    st.markdown(
        """
        <div class="chat-header">
          <h2 style="margin:0;">💬 Chatbot</h2>
          <div style="color:#9ca3af;margin-top:6px;">
            OpenAI Chat API 기반. 좌측 사이드바에서 모델·온도·시스템프롬프트를 조절하세요.
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- 사이드바(설정/유틸) ----------
with st.sidebar:
    st.subheader("환경 설정")
    # API Key: secrets 우선, 없으면 입력값
    default_key = st.secrets.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input("OpenAI API Key", value=default_key, type="password", help="secrets.toml에 저장하면 자동으로 불러옵니다.")
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
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심을 굵게 강조하고, 불필요한 수사는 피하세요.",
        height=100
    )

    st.divider()
    col_a, col_b = st.columns(2)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True)
    download_ready = col_b.button("내려받기(JSON)", use_container_width=True)

# ---------- 상태 초기화 ----------
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ---------- OpenAI 클라이언트 ----------
def get_client() -> OpenAI | None:
    key = api_key_input.strip()
    if not key:
        return None
    return OpenAI(api_key=key)

client = get_client()

# ---------- 유틸: 스트리밍 제너레이터 ----------
def stream_completion_text(client, msgs, model, temperature, max_tokens):
    resp = client.chat.completions.create(
        model=model,
        messages=msgs,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
    )
    for ch in resp:
        if ch.choices and getattr(ch.choices[0].delta, "content", None):
            yield ch.choices[0].delta.content  # 문자열만 yield


# ---------- 기존 메시지 렌더 ----------
def render_message(role: str, content: str, when: str | None = None):
    meta = when or datetime.now().strftime("%H:%M")
   with st.chat_message("assistant", avatar="🤖"):
    response_text = st.write_stream(
        stream_completion_text(client, history, model, temperature, max_tokens)
    )
st.session_state.messages.append(
    {"role": "assistant", "content": response_text, "time": datetime.now().strftime("%H:%M")}
)

# ---------- 키 유효성 안내 ----------
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하세요. `secrets.toml`에 저장하면 자동 로드됩니다.", icon="🔐")

# ---------- 채팅 입력 ----------
prompt = st.chat_input("메시지를 입력하세요…")

if prompt and client:
    # 시스템 프롬프트 + 히스토리 + 유저 메시지 구성
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})
    history.extend(st.session_state.messages)
    user_msg = {"role": "user", "content": prompt}
    history.append(user_msg)

    # 화면에 유저 메시지 먼저 출력
    render_message("user", prompt)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    # 스트리밍 생성
    with st.chat_message("assistant", avatar="🤖"):
        acc = []
        for token in stream_completion(client, history):
            acc.append(token)
            st.markdown(
                f'<div class="msg bot"><div class="meta">assistant · {datetime.now().strftime("%H:%M")}</div>'
                f'{"".join(acc)}</div>',
                unsafe_allow_html=True
            )
            # 동일 영역 갱신을 위해 empty/placeholder를 써도 되지만,
            # 간단히 재렌더링 방식을 유지(성능 이슈 없으면 OK)

        assistant_text = "".join(acc) if acc else "(응답 없음)"
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text, "time": datetime.now().strftime("%H:%M")}
    )

# ---------- 내려받기 ----------
if download_ready:
    fname = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    st.download_button(
        "대화 내용 저장",
        data=json.dumps(st.session_state.messages, ensure_ascii=False, indent=2),
        file_name=fname,
        mime="application/json",
        use_container_width=True
    )
    st.caption("대화 기록을 JSON으로 저장했습니다.")

# ---------- 풋터 힌트 ----------
st.markdown("<hr/>", unsafe_allow_html=True)
st.caption("힌트: 설정은 사이드바에서 조절하세요. 실행은 `python -m streamlit run app_chat_pretty.py`가 가장 안정적입니다.")
