# streamlit_app.py
from __future__ import annotations
import json
from datetime import datetime
from typing import Dict, List, Generator, Optional
import re

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

# ── CSS ────────────────────────────────────────────────────────────────────────
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
.stButton>button{
  background: linear-gradient(90deg, #34d399, #10b981);
  border:0; color:white; font-weight:700;
  box-shadow: 0 4px 14px rgba(16,185,129,.25);
}
.stButton>button:hover{filter:brightness(1.04);}
.msg{border:1px solid var(--border); padding:14px 16px; border-radius:14px; margin:8px 0; line-height:1.55;}
.msg.user{background-color: var(--user);}
.msg.bot{background-color: var(--bot);}
.msg .meta{font-size:12px; color:var(--muted); margin-bottom:6px;}
</style>
""", unsafe_allow_html=True)

# ── 헤더 ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="chat-header">
      <h2 style="margin:0;">💬 Chatbot</h2>
      <div style="color:#6b7280;margin-top:6px;">
        OpenAI Chat API 기반. 좌측에서 모델/온도/시스템프롬프트를 조절하세요.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ── 유틸 함수 ─────────────────────────────────────────────────────────────────
def strip_md(s: str) -> str:
    """굵게/이탤릭 마크다운(**, *, __, _) 제거"""
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s, flags=re.S)
    s = re.sub(r"\*(.*?)\*", r"\1", s)
    s = re.sub(r"__(.*?)__", r"\1", s, flags=re.S)
    s = re.sub(r"_(.*?)_", r"\1", s)
    return s.replace("**", "")

def render_message(role: str, content: str, when: Optional[str] = None):
    meta = when or datetime.now().strftime("%H:%M")
    with st.chat_message("assistant" if role=="assistant" else "user",
                         avatar="🤖" if role=="assistant" else "🧑"):
        st.markdown(
            f'<div class="msg {"bot" if role=="assistant" else "user"}">'
            f'<div class="meta">{role} · {meta}</div>{strip_md(content)}</div>',
            unsafe_allow_html=True
        )

# ── 세션 초기화 ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str,str]] = []
if "__main_task_area" not in st.session_state:
    st.session_state["__main_task_area"] = ""
if "__clear_main" not in st.session_state:
    st.session_state["__clear_main"] = False
if "__ctx_mode" not in st.session_state:
    st.session_state["__ctx_mode"] = "이전 대화 무시"
if st.session_state["__clear_main"]:
    st.session_state["__main_task_area"] = ""
    st.session_state["__clear_main"] = False

# ── 사이드바 ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.subheader("환경 설정")

    key_default = st.session_state.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input("OpenAI API Key", value=key_default, type="password",
        help="OpenAI API Key를 입력하세요. 세션에 저장되어 새로고침 전까지 유지됩니다.")

    model = st.selectbox(
        "Model",
        ["gpt-4o-mini","gpt-4o","gpt-4.1-mini","gpt-3.5-turbo"],
        index=0,
        help="모델 종류 선택\n- 4o-mini: 빠르고 저렴\n- 4o: 고품질\n- 3.5/4.1-mini: 비용 절감"
    )
    temperature = st.slider("Temperature",0.0,1.2,0.7,0.1,
        help="창의성 조절: 낮을수록 일관성↑, 높을수록 다양성/창의성↑")
    max_tokens = st.slider("Max tokens(응답)",256,4096,1024,64,
        help="모델이 한 번에 생성할 최대 토큰 수. 값↑ = 긴 응답 가능")
    system_prompt = st.text_area("System prompt",
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 명확하게 강조합니다.",
        height=100,
        help="모델의 기본 성격과 말투를 정의합니다.")

    st.divider()
    col_a,col_b = st.columns(2)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True)
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True)

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ── OpenAI Client ──────────────────────────────────────────────────────────
def get_client() -> Optional[OpenAI]:
    if api_key_input: st.session_state["OPENAI_API_KEY"]=api_key_input.strip()
    key = st.session_state.get("OPENAI_API_KEY","").strip()
    if not key: return None
    try: return OpenAI(api_key=key)
    except: return None

client=get_client()

# ── 스트리밍 ───────────────────────────────────────────────────────────────
def stream_completion_text(_client:OpenAI,_messages:List[Dict[str,str]],_model:str,_temperature:float,_max_tokens:int)->Generator[str,None,None]:
    resp=_client.chat.completions.create(model=_model,messages=_messages,temperature=_temperature,max_tokens=_max_tokens,stream=True)
    for chunk in resp:
        if chunk.choices and getattr(chunk.choices[0].delta,"content",None):
            yield chunk.choices[0].delta.content

def write_stream_safe(gen:Generator[str,None,None])->str:
    ph=st.empty();acc=[]
    for tok in gen:
        acc.append(tok)
        safe=strip_md("".join(acc))
        ph.markdown(f'<div class="msg bot"><div class="meta">assistant · {datetime.now():%H:%M}</div>{safe}</div>',unsafe_allow_html=True)
    return strip_md("".join(acc))

# ── 과거 메시지 렌더링 ──────────────────────────────────────────────────────
for m in st.session_state.messages:
    render_message(m["role"],m["content"],m.get("time"))

# ── 자유 입력 ───────────────────────────────────────────────────────────────
user_input = st.chat_input("메시지를 입력하세요…")
if user_input and client:
    history=[{"role":"system","content":system_prompt.strip()}] if system_prompt.strip() else []
    history.extend(st.session_state.messages)
    user_msg={"role":"user","content":user_input}
    history.append(user_msg)
    render_message("user",user_input)
    st.session_state.messages.append({**user_msg,"time":datetime.now().strftime("%H:%M")})
    with st.chat_message("assistant",avatar="🤖"):
        response_text=write_stream_safe(stream_completion_text(client,history,model,temperature,max_tokens))
    st.session_state.messages.append({"role":"assistant","content":response_text,"time":datetime.now().strftime("%H:%M")})

# ── 메인 프롬프트 박스 ──────────────────────────────────────────────────────
st.markdown("<hr/>",unsafe_allow_html=True)
st.markdown("#### 프롬프트")
main_text=st.text_area("입력창",key="__main_task_area",height=160,label_visibility="collapsed",placeholder="텍스트를 입력하세요…")
ctx_mode=st.radio("컨텍스트",["대화 연속","이전 대화 무시"],index=1,key="__ctx_mode")

c1,c2,c3,c4=st.columns(4)
send_prompt=None;action=None

def guard_empty():
    if not main_text.strip():
        st.warning("프롬프트가 비었습니다.");return True
    return False

if c1.button("요약(3줄)",use_container_width=True):
    if not guard_empty(): send_prompt="아래 텍스트를 3줄로 요약:\n\n"+main_text;action="sum"
if c2.button("번역",use_container_width=True):
    if not guard_empty(): send_prompt="아래 텍스트를 번역:\n\n"+main_text;action="tr"
if c3.button("코드 리뷰",use_container_width=True):
    if not guard_empty(): send_prompt="아래 코드 리뷰:\n\n"+main_text;action="rev"
if c4.button("그대로 보내기",use_container_width=True):
    if not guard_empty(): send_prompt=main_text;action="raw"

if send_prompt and client:
    history=[{"role":"system","content":system_prompt.strip()}] if system_prompt.strip() else []
    if st.session_state["__ctx_mode"]=="대화 연속": history.extend(st.session_state.messages)
    history.append({"role":"user","content":send_prompt})
    render_message("user",send_prompt)
    st.session_state.messages.append({"role":"user","content":send_prompt,"time":datetime.now().strftime("%H:%M")})
    with st.chat_message("assistant",avatar="🤖"):
        response_text=write_stream_safe(stream_completion_text(client,history,model,temperature,max_tokens))
    st.session_state.messages.append({"role":"assistant","content":response_text,"time":datetime.now().strftime("%H:%M")})
    st.session_state["__clear_main"]=True
    st.rerun()

# ── 내려받기 ────────────────────────────────────────────────────────────────
if download_clicked:
    fname=f"chat_{datetime.now():%Y%m%d_%H%M%S}.json"
    st.download_button("대화 저장",data=json.dumps(st.session_state.messages,ensure_ascii=False,indent=2),file_name=fname,mime="application/json")
