콘텐츠로 건너뛰기
채팅 기록

나의 말:
https://chatbot-dori.streamlit.app/

이 코드를 어디서 찾아야 하지? 윈드서프에서 어떻게 검색을 해야하나
ChatGPT의 말:
좋은 질문이에요. 정리해 드릴게요.

1. 지금 주소(https://chatbot-dori.streamlit.app/)는
배포된 Streamlit Cloud 앱 주소예요.

여기에는 실행된 결과 화면만 보이고, 실제 소스 코드는 보이지 않아요.

따라서 코드를 찾으려면 Streamlit Cloud에 로그인해서 본인이 올린 저장소(GitHub 등)와 연결된 부분을 확인해야 해요.

2. 코드가 어디에 있나?
보통 Streamlit Cloud에서 앱을 띄울 때는

GitHub 저장소(레포)와 연결하거나,

직접 .py 파일을 업로드해서 실행해요.

따라서 소스 코드는 GitHub 저장소 또는 윈드서프(Windsurf IDE) 프로젝트 안에 있어요.

3. 윈드서프에서 찾는 방법
윈드서프는 보통 GitHub와 연동해서 작업하니까, 코드 찾는 순서는 이렇게 하시면 돼요:

윈드서프에서 GitHub 레포 열기

사이드바에서 Source Control 아이콘 클릭 → 연결된 GitHub 레포 확인.

파일명으로 검색하기

단축키: Ctrl + P (Quick Open)

보통 streamlit_app.py 또는 app.py라는 이름을 써요.

검색창에 streamlit_app.py 또는 app.py 입력.

코드 내용으로 검색하기

단축키: Ctrl + Shift + F (전체 검색)

예: st.set_page_config 또는 st.title 같은 Streamlit 전용 함수 검색.

이렇게 하면 Streamlit 관련 코드 파일을 바로 찾을 수 있어요.

👉 도리, 혹시 제가 바로 윈드서프에서 chatbot-dori 프로젝트 소스 위치를 검색해 드릴까요?
아니면 GitHub 주소를 연결해 둔 게 있나요?

나의 말:
https://github.com/DoriChoi/chatbot_250904_dori

요기에 있어 다만 윈드서프에서 수정해서 다시 업데이트 하려고 하는데 기존 소스가 어디 있는지 모르겠어
ChatGPT의 말:
좋아요, 이제 그림이 조금 더 명확해졌네요. 도리의 상황을 정리하면:

앱 주소: https://chatbot-dori.streamlit.app/ → 이건 실행 화면일 뿐, 코드 위치는 안 보임.

실제 코드 저장소: https://github.com/DoriChoi/chatbot_250904_dori → 여기 안에 있음.

목표: 윈드서프(Windsurf IDE)에서 이 저장소 코드를 열고 수정 후 다시 배포.

1. 코드가 어디 있는지
해당 GitHub 저장소 안에서 Streamlit 앱은 보통 streamlit_app.py 혹은 **app.py**라는 이름의 파일에 있어요.
👉 윈드서프에서 검색할 때는:

단축키 Ctrl + P → streamlit_app.py 입력 (파일명 검색)

단축키 Ctrl + Shift + F → st.set_page_config 같은 Streamlit 전용 함수로 검색 (내용 검색)

이렇게 하면 소스 파일이 바로 잡힐 거예요.

2. 윈드서프에서 기존 소스 찾기
윈드서프에서는 GitHub와 연결된 레포를 불러와야 해요.

윈드서프 시작 화면 → "Clone from GitHub" 선택

https://github.com/DoriChoi/chatbot_250904_dori 주소 붙여넣기

로컬에 내려받은 후, 왼쪽 파일 탐색기에서 streamlit_app.py 같은 파일을 열면 됨

3. 업데이트 & 배포 절차
윈드서프에서 코드 수정

GitHub에 commit & push

Streamlit Cloud에서 해당 GitHub 저장소와 연결되어 있으면 자동으로 새 버전 배포됨

👉 도리, 제가 GitHub 저장소 구조를 직접 열어서 streamlit_app.py가 정확히 어디 있는지 확인해 드릴까요? (예: / 루트에 있는지, app/ 폴더 안에 있는지)

나의 말:
ㅇㅇ
ChatGPT의 말:
코드 구조 봤고, streamlit_app.py 파일이 레포 루트에 있어요. 
GitHub

📂 파일 위치 요약
chatbot_250904_dori/
  ├── .devcontainer/
  ├── .github/
  ├── .gitignore
  ├── LICENSE
  ├── README.md
  ├── requirements.txt
  └── **streamlit_app.py**
✅ 당신이 해야 할 일 (윈드서프에서 수정 → 배포)
윈드서프에서 GitHub 레포 DoriChoi/chatbot_250904_dori 클론

streamlit_app.py 파일 열기

코드 수정

커밋 & 푸시 (GitHub에 적용)

Streamlit Cloud 배포 자동 혹은 수동 리빌드

필요하면 각 단계 더 구체적으로 도와드릴까요?

나의 말:
1
ChatGPT의 말:
좋습니다, 도리. 그럼 **1단계 (윈드서프에서 GitHub 레포 클론하기)**를 자세히 알려드릴게요.

1. GitHub 레포 클론 (윈드서프에서)
윈드서프 실행
→ 첫 화면 또는 상단 메뉴에서 “Clone Repository” 선택

GitHub URL 입력

https://github.com/DoriChoi/chatbot_250904_dori.git
저장 위치 선택
→ 로컬에 저장할 폴더 지정

클론 완료 후, 왼쪽 파일 탐색기에 프로젝트 구조가 나타납니다.
→ 여기서 streamlit_app.py 파일 확인 가능

👉 여기까지 하면 로컬에 코드가 준비돼요.
도리, 원하시면 제가 2단계 (streamlit_app.py 파일 열기 → 수정) 방법도 이어서 알려드릴까요?

나의 말:
→ 첫 화면 또는 상단 메뉴에서 “Clone Repository” 선택

이게 안 보여 어디에 있는거야?
ChatGPT의 말:
도리, 윈드서프 첫 화면에서 **“Clone Repository”**가 안 보이는 건 환경에 따라 UI가 다르기 때문이에요. 대신 이렇게 찾아보세요:

1. Command Palette에서 실행
단축키: Ctrl + Shift + P (맥이면 Cmd + Shift + P)

검색창에 Clone 입력 → Git: Clone 선택

여기서 GitHub URL (https://github.com/DoriChoi/chatbot_250904_dori.git) 넣으면 돼요.

2. 메뉴 경로로 접근
상단 메뉴에서

File → Add Folder to Workspace 로 클론한 폴더를 열거나

Source Control (왼쪽 사이드바 git 아이콘) → Clone Repository 버튼 찾기

3. 로컬 폴더 직접 열기
이미 PC에 git clone으로 받아놨다면:

File → Open Folder... 로 해당 프로젝트 폴더 열면 됨.

👉 도리, 지금 PC에 git 설치는 되어 있나요?
없으면 먼저 git 설치해야 Clone Repository가 제대로 보일 수 있어요.

나의 말:
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
    col_a, col_b, col_c = st.columns(3)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True)
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True)
    examples_toggle = col_c.toggle("추천 질문", value=False)

# ── 세션 상태 ────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ── OpenAI 클라이언트: 입력값→세션에 고정 저장 + 예외 처리 ────────────────────
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

# ── 추천 질문(클릭 시 즉시 전송) ───────────────────────────────────────────────
suggestion: Optional[str] = None
if examples_toggle:
    st.caption("클릭하면 바로 전송됩니다.")
    c1, c2, c3 = st.columns(3)
    if c1.button("요약해줘(3줄)", use_container_width=True):
        suggestion = "아래 텍스트를 3줄로 요약해줘:\n\n"
    if c2.button("영→한 번역", use_container_width=True):
        suggestion = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n"
    if c3.button("코드 리뷰", use_container_width=True):
        suggestion = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n"

# ── 키 안내 ───────────────────────────────────────────────────────────────────
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하면 세션에 저장되어 계속 사용됩니다.", icon="🔐")

# ── 채팅 입력 (※ chat_input에는 default/value 없음) ──────────────────────────
user_input = None if suggestion else st.chat_input("메시지를 입력하세요…")
final_prompt = suggestion or user_input

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

오류가 있는데 추천 질문 기능이 프롤프트 이후에 나와야 하는데 먼저 나와버림 이걸 수정해야 해
ChatGPT의 말:

57s 동안 생각함
도리, 원인과 처방을 딱 정리할게.

문제 원인

추천 질문 UI가 **사이드바 바깥(메인 영역)**에서 그려지고, 코드상 chat_input 보다 먼저 호출돼서 화면 상단에 뜹니다.

Streamlit은 호출 순서대로 렌더링되고, st.chat_input은 기본적으로 하단에 고정됩니다. 따라서 메인 영역에선 chat_input “아래”로 보이게 둘 수 없어요. 
Streamlit
+2
Streamlit Docs
+2

해결 핵심

추천 질문 버튼을 사이드바 안(시스템 프롬프트 아래)으로 옮기고, 클릭 시 값을 세션 상태에 넣은 뒤 즉시 소비(pop) 하도록 바꿔 중복 전송을 방지합니다.

아래처럼 최소 수정하세요.

1) 사이드바에 “추천 질문” 버튼 배치 (System prompt 아래)
with st.sidebar: 블록 끝나기 전에 다음을 넣고, 기존의 col_c.toggle("추천 질문"...은 그대로 써도 됩니다(토글 유지):

# (사이드바 내부, system_prompt 정의 아래에 위치)
examples_toggle = st.toggle("추천 질문", value=False)

if examples_toggle:
    st.caption("클릭하면 바로 전송됩니다.")
    # 버튼 키는 고유하게
    if st.button("요약해줘(3줄)", use_container_width=True, key="sug_sum"):
        st.session_state["__suggestion"] = "아래 텍스트를 3줄로 요약해줘:\n\n"
    if st.button("영→한 번역", use_container_width=True, key="sug_tr"):
        st.session_state["__suggestion"] = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n"
    if st.button("코드 리뷰", use_container_width=True, key="sug_rev"):
        st.session_state["__suggestion"] = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n"
else:
    # 토글을 끄면 잔여 제안값 제거
    st.session_state.pop("__suggestion", None)
2) 메인 영역의 기존 “추천 질문” 블록 삭제
아래 블록을 완전히 제거하세요:

# ── 추천 질문(클릭 시 즉시 전송) ───────────────────────────────────────────────
suggestion: Optional[str] = None
if examples_toggle:
    st.caption("클릭하면 바로 전송됩니다.")
    c1, c2, c3 = st.columns(3)
    ...
3) chat_input 직전에 제안값 ‘한 번만’ 소비(pop)
chat_input 바로 위에 다음 한 줄 넣으세요:

suggestion: Optional[str] = st.session_state.pop("__suggestion", None)
그리고 기존 로직 유지:

user_input = None if suggestion else st.chat_input("메시지를 입력하세요…")
final_prompt = suggestion or user_input
이렇게 하면

**추천 질문 UI는 시스템 프롬프트 ‘이후’(사이드바 아래)**에 나오고,

클릭 시 즉시 전송, 재실행 후에는 pop() 덕분에 중복 발화 없음,

메인 영역은 깔끔하게 대화 + 입력창만 유지됩니다.

근거

Streamlit은 코드 호출 순서대로 렌더링되며, 레이아웃 제어는 container/empty로 우회 가능하지만 st.chat_input은 기본적으로 하단 고정 동작을 갖습니다. 
Streamlit
+1

st.chat_input의 위치/행태(하단 고정, 컨테이너 안에 넣으면 인라인로 동작)는 공식 문서/커뮤니티 토론에 정리돼 있습니다. 
Streamlit Docs
+1

필요하면 내가 패치 버전 전체 파일로 정리해서 붙여줄게.

나의 말:
ㅇㅇ
ChatGPT의 말:
좋아, 전체 파일 교체본 바로 줍니다. 핵심은 추천 질문 UI를 사이드바의 시스템 프롬프트 ‘아래’로 이동하고, 클릭 시 값을 세션에 넣었다가 한 번만 소비(pop) 하도록 바꾼 것.

아래 내용을 그대로 streamlit_app.py로 덮어쓰세요.

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

    # ── [수정 포인트] 추천 질문: 시스템 프롬프트 '아래'에 위치 ───────────────
    st.markdown("#### 추천 질문")
    examples_toggle = st.toggle("패널 열기", value=False)
    if examples_toggle:
        st.caption("클릭하면 바로 전송됩니다.")
        if st.button("요약해줘(3줄)", use_container_width=True, key="sug_sum"):
            st.session_state["__suggestion"] = "아래 텍스트를 3줄로 요약해줘:\n\n"
        if st.button("영→한 번역", use_container_width=True, key="sug_tr"):
            st.session_state["__suggestion"] = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n"
        if st.button("코드 리뷰", use_container_width=True, key="sug_rev"):
            st.session_state["__suggestion"] = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n"
    else:
        # 토글을 끄면 잔여 제안값 제거
        st.session_state.pop("__suggestion", None)

# ── 세션 상태 ────────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

if clear_clicked:
    st.session_state.messages = []
    st.rerun()

# ── OpenAI 클라이언트: 입력값→세션에 고정 저장 + 예외 처리 ────────────────────
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

# ── [수정 포인트] 추천 질문 값 한 번만 소비 ───────────────────────────────────
suggestion: Optional[str] = st.session_state.pop("__suggestion", None)

# ── 키 안내 ───────────────────────────────────────────────────────────────────
if client is None:
    st.info("사이드바에 **OpenAI API Key**를 입력하면 세션에 저장되어 계속 사용됩니다.", icon="🔐")

# ── 채팅 입력 (※ chat_input에는 default/value 없음) ──────────────────────────
user_input = None if suggestion else st.chat_input("메시지를 입력하세요…")
final_prompt = suggestion or user_input

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
핵심 변경점

추천 질문 블록을 사이드바로 이동: 시스템 프롬프트 바로 아래.

버튼 클릭 시 st.session_state["__suggestion"]에 저장 → 메인에서 pop()으로 한 번만 소비.

메인 영역의 기존 추천 질문 열(Column) 블록은 제거.

원하는 동작 맞는지 바로 테스트해보고, 필요하면 더 다듬자.

나의 말:
윈드서프에서 불러와서 코드 수정했어 이제 깃허브에 적용하는 법
ChatGPT의 말:
좋습니다 👍 이제 윈드서프에서 수정한 코드를 GitHub에 적용(=커밋 + 푸시) 하는 방법을 차근차근 알려드릴게요.

1. 변경된 파일 확인
왼쪽 사이드바에서 Source Control (Git 아이콘) 클릭

수정된 파일(streamlit_app.py)이 목록에 보일 거예요.

2. 커밋(commit)
상단에 메시지 입력란이 있어요 → 추천 질문 UI 사이드바 이동 같은 간단한 설명 입력

그 아래 ✔ Commit 버튼 클릭

3. 원격 저장소로 푸시(push)
커밋 후, 상단에 Sync Changes 또는 Push 버튼이 뜰 거예요.

그걸 클릭하면 GitHub(DoriChoi/chatbot_250904_dori)에 코드가 올라갑니다.

4. Streamlit Cloud 배포
이 레포(chatbot_250904_dori)와 Streamlit Cloud가 연결되어 있으면,
GitHub에 푸시된 순간 자동으로 새 버전 배포가 진행됩니다.

배포 로그는 Streamlit Cloud Dashboard에서 확인 가능해요.

만약 Push 버튼이 안 보인다?
터미널 열고 직접 입력할 수도 있어요:

git add .
git commit -m "추천 질문 UI 사이드바로 이동"
git push origin main
(브랜치명이 main이 아니라 master라면 main 대신 master 입력)

👉 도리, 지금 윈드서프에서 Source Control(Git 아이콘) 메뉴가 보이나요? 아니면 제가 터미널 명령어 방식으로 진행하는 게 더 편할까요?

나의 말:
코밋을 하는데 왜 이렇게 오래걸려
ChatGPT의 말:
좋은 질문이에요. 도리 상황을 정리하면: 윈드서프에서 커밋 버튼을 눌렀는데, 반응이 느리고 오래 걸린다는 거죠.

✅ 커밋이 오래 걸리는 주요 원인
프로젝트 용량 문제

대용량 파일(예: 캐시, 데이터, 이미지, 가상환경 폴더)이 같이 잡혀 있으면 Git이 압축·기록하느라 시간이 많이 걸려요.

특히 .gitignore에 venv/, .streamlit/, .env, __pycache__/ 등을 안 넣으면 이런 현상 생깁니다.

네트워크 지연 아님

"Commit"은 로컬 Git DB에 저장하는 동작이라 원래 순간적으로 끝나야 정상입니다.

오래 걸린다면, 실제로는 "Push"까지 같이 시도되거나, Git이 대용량 변경분을 처리 중인 거예요.

Windsurf UI 특성

일부 IDE는 "Commit & Push"를 한 번에 실행합니다. 이 경우 GitHub로 업로드까지 걸리니 느려질 수 있어요.

✅ 해결 방법
변경된 파일만 커밋

Source Control에서 꼭 필요한 파일(streamlit_app.py)만 체크하고 커밋하세요.

venv, .env, .streamlit 등은 체크 해제.

.gitignore 추가
루트에 .gitignore 파일을 만들어 아래 내용 넣으세요:

__pycache__/
.env
.streamlit/
venv/
.DS_Store
이렇게 하면 불필요한 파일이 아예 Git에 안 잡힙니다.

분리해서 작업

먼저 git commit (빠름)

그다음 git push (네트워크 속도 따라 느릴 수 있음)

👉 도리, 지금 Commit 단계에서 오래 걸리는 건지, 아니면 Push까지 같이 하는 건지 확인해 줄 수 있어요?
(예: "커밋 누르면 바로 GitHub에 올라가고 있던데요" or "아직 로컬 커밋인데도 1분 넘게 걸림")

나의 말:
업로드한 이미지
여전히 같은 문제 발생... 추천 질문을 열면 프롬프트 아래에 있든지 아니면 프롬프트 작성 후 선택하면 그걸 요약이나 번역해 줘야 하는데 안돼
ChatGPT의 말:

17s 동안 생각함
도리, 결론부터.

핵심 문제

st.chat_input는 값을 미리 채우거나, 위치를 마음대로 옮길 수 없습니다. 버튼으로 프롬프트를 “세팅”해 넣는 방식이 불가라 지금처럼 동작이 어긋납니다. 
Streamlit
+2
Streamlit Docs
+2

정확한 처방

별도 입력란(텍스트 영역) + 액션 버튼으로 “작업 대상 텍스트”를 받음 → 버튼(요약/번역/리뷰) 클릭 시 즉시 메시지로 발송(chat_input 우회).

세션키(__suggestion, __task_text)를 사용해 클릭 직후 한 번만 소비(pop).

아래 패치를 그대로 넣으면,

사이드바에서 텍스트를 붙여넣고

요약/번역/리뷰를 누르면

그 조합으로 바로 대화에 전송됩니다.

변경 패치(필요 부분만 교체)
1) 사이드바: “추천 질문” 블록을 텍스트 입력 + 액션 버튼으로 변경
with st.sidebar: 내부, 시스템 프롬프트 아래에 다음으로 바꿔 넣으세요(기존 추천 질문 블록은 삭제).

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
2) 메인 영역: 버튼 클릭 시 즉시 발화되도록 조합
# ── [수정 포인트] 추천 질문 값 한 번만 소비 아래를 다음처럼 확장:

suggestion: Optional[str] = st.session_state.pop("__suggestion", None)
task_text_mem: Optional[str] = st.session_state.pop("__task_text", None)

# suggestion이 있으면 chat_input 대신 즉시 전송용 prompt 구성
if suggestion:
    combined = suggestion + (task_text_mem or "")
else:
    combined = None
그리고 기존 입력부를 아래처럼 교체:

# chat_input은 여전히 하단 입력 전용
user_input = None if combined else st.chat_input("메시지를 입력하세요…")
final_prompt = combined or user_input
이렇게 하면,

프롬프트를 먼저 작성 → 버튼 클릭 흐름이 완벽히 성립합니다(버튼 직후 전송).

chat_input은 그대로 “자유 대화 입력” 용도로 유지됩니다.

왜 이렇게 해야 하나(근거)
st.chat_input은 프로그램이 값을 주입하는 기능이 없습니다(세션으로도 불가). 또한 메인 영역 하단 고정 성격이라 위치 제어도 제한됩니다. 따라서 “작성 후 버튼으로 chat_input을 채워 넣는 UX”는 구조적으로 불가능합니다. 위 우회가 정석입니다. 
Streamlit
+1

스트리밍은 st.write_stream으로 현재 구현이 맞습니다(버전 호환 주의). 
Streamlit Docs
+1

원하는 동작대로 안 되면, 내가 완성본 전체 파일 형태로 다시 정리해서 붙여줄게.
필요하면 “요약 길이(문장 수)” 슬라이더, “번역 방향” 라디오까지 바로 붙여줄 수 있어.

나의 말:
ㅇㅇ
ChatGPT의 말:
좋아. 전체 교체본 바로 준다. 핵심은 사이드바에서 텍스트를 붙여넣고(작업 대상 텍스트), 요약/번역/리뷰 버튼을 누르면 즉시 발화되도록 구성했다. st.chat_input은 그대로 자유 입력용이다.

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
핵심 요약

추천 패널에 텍스트 입력칸 추가 → 버튼 클릭 시 __suggestion + __task_text를 세션에 저장.

메인에서 이를 pop()으로 한 번만 소비 → final_prompt로 즉시 전송.

st.chat_input은 자유 입력 전용.

원하는 UX로 동작할 거다. 필요하면 요약 문장 수 슬라이더, 번역 방향(한→영/영→한) 옵션도 추가해줄게.

나의 말:
업로드한 이미지
추천 질문이 옆에 따로 넣는게 아니라 메인 프롬프트 창 아래에 달려서 창에 정보를 넣고 누르면 바로 값이 나오게 해야 해
ChatGPT의 말:

18s 동안 생각함
도리, 정확히 말하면 st.chat_input 아래에 버튼을 “붙이는” 건 불가능합니다.
st.chat_input은 값 주입·UI 확장 불가(기본값/프리필 없음, 위치 고정)라서요. 공식 문서/이슈에 명시되어 있습니다. 
Streamlit
+3
Streamlit Docs
+3
Streamlit Docs
+3

그래서 **메인 영역 맨 아래(푸터 위)**에 우리가 직접 만든 “커스텀 입력 박스(텍스트영역+액션 버튼)”를 배치하는 방식이 사실상 유일한 해결책입니다. st.chat_input은 자유 채팅용으로 남겨두고, 요약/번역/리뷰는 커스텀 박스에서 즉시 발화되도록 합시다.

아래 패치만 추가하면, 화면 흐름이 대화 → (맨 아래) 메인 프롬프트 박스 → 버튼 클릭 시 즉시 응답 으로 바뀝니다.

코드 패치 (핵심만 추가·교체)
사이드바의 추천 패널은 삭제(이미 메인으로 옮길 것이므로).

**메인 영역 “푸터 바로 위”**에 커스텀 입력 박스 추가
# ── 빌드 태그(배포 반영 확인용) 직전에 아래 블록을 넣으세요.

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

# 커스텀 박스에서 눌렀다면 chat_input 대신 즉시 전송
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
    st.rerun()
기존 입력부는 그대로 유지

st.chat_input("메시지를 입력하세요…")는 자유 채팅용.

커스텀 박스 버튼을 누르면 위 로직이 즉시 전송하고 st.rerun()으로 화면을 갱신합니다.

왜 이 방식이 정답인가
st.chat_input은 한 페이지 1개 제한 + 메인 영역 고정이고, 값을 외부에서 채워 넣는 API가 없음. 그래서 “프롬프트 아래 버튼” 같은 확장형 UI는 사용자 정의 컨테이너로 구현해야 합니다. 
Streamlit Docs
+2
Streamlit Docs
+2

스트리밍은 st.write_stream으로 구현해 최종 문자열을 받아 세션 히스토리에 저장하는 현재 구조가 맞습니다. 
Streamlit Docs
+1

원하는 “메인 프롬프트 창 아래 버튼 → 누르면 바로 결과”가 딱 이렇게 동작합니다.
필요하면 여기에 요약 문장 수 슬라이더, 번역 방향(한↔영) 라디오, 프롬프트 프리셋 드롭다운도 붙여서 확장해 줄게.

나의 말:
ㅇㅇ
ChatGPT의 말:

4초 동안 생각함
좋아. 메인 프롬프트 박스 아래에 버튼이 붙고, 누르면 즉시 응답되도록 전체 파일 버전 붙인다. 사이드바의 추천 패널은 제거했고, 메인 영역 맨 아래에 **텍스트박스 + 액션 버튼(요약/번역/리뷰/그대로 보내기)**를 넣었다.

근거: Streamlit의 st.chat_input은 기본값 주입/위치 변경이 불가(하단 고정형). 따라서 확장형 입력 UI는 메인 컨테이너에 사용자 정의 텍스트 영역 + 버튼으로 구현해야 한다는 제약이 있다(공식 위젯 스펙).

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
포인트

메인 입력 박스를 대화 영역 맨 아래에 배치 → 버튼 클릭 시 즉시 발화 → st.rerun()으로 새 상태 반영.

st.chat_input은 자유 채팅 전용으로 유지(필요 시 이후 제거 가능).

문제 없으면 이대로 커밋/푸시(→ Streamlit Cloud 자동 배포)하면 된다.

나의 말:
업로드한 이미지
한영 번역이 안되고 프롬프트에 대한 결과값이 나온 후에는 프롬프트 창이 비어 있어야 하는데 기존 프롬프트가 그대로 남아있음 오류 수정해줘
ChatGPT의 말:

17s 동안 생각함
좋아, 두 가지를 정확히 고친다.

번역 방향 선택 추가(영→한 / 한→영) → 너가 한국어 텍스트를 넣고 “영→한”을 눌러도 변환이 안 되는 문제 해결.

응답 후 프롬프트 비우기 → 결과가 나오면 메인 텍스트박스를 즉시 초기화.

아래 패치 부분만 적용하면 된다(전체파일 교체 불필요).

1) 메인 프롬프트 박스에 “번역 방향” 라디오 추가 + 버튼 로직 수정
# ── 메인 프롬프트 박스(텍스트 + 액션 버튼) ── 블록을 다음처럼 바꿔줘.

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

    # 번역 방향 선택 (영→한 / 한→영)
    trans_dir = st.radio(
        "번역 방향",
        options=("영→한", "한→영"),
        horizontal=True,
        key="__trans_dir"
    )

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None

    # 빈 입력 방지
    def guard_empty():
        if not (main_text or "").strip():
            st.warning("프롬프트가 비어 있습니다. 텍스트를 입력하세요.", icon="⚠️")
            return True
        return False

    if c1.button("요약(3줄)", use_container_width=True, key="main_sum"):
        if not guard_empty():
            send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + main_text

    if c2.button("번역", use_container_width=True, key="main_tr"):
        if not guard_empty():
            if trans_dir == "영→한":
                send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + main_text
            else:  # 한→영
                send_prompt = "아래 한국어 문장을 자연스러운 영어로 번역해줘:\n\n" + main_text

    if c3.button("코드 리뷰", use_container_width=True, key="main_rev"):
        if not guard_empty():
            send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + main_text

    if c4.button("그대로 보내기", use_container_width=True, key="main_send"):
        if not guard_empty():
            send_prompt = main_text
2) 전송 직후 텍스트박스 비우기
같은 블록 아래의 전송 처리부(현재 if send_prompt and client: 이하)에 초기화 한 줄을 추가:

if send_prompt and client:
    # ... (히스토리 구성/스트리밍 그대로)
    st.session_state.messages.append(
        {"role": "assistant", "content": response_text or "(응답 없음)", "time": datetime.now().strftime("%H:%M")}
    )

    # >>> 프롬프트 초기화 (중요)
    st.session_state["__main_task_area"] = ""

    st.rerun()
이렇게 하면,

번역은 선택한 방향대로 작동하고,

응답이 끝나면 입력칸이 즉시 비워진다(세션 스테이트로 위젯 값을 리셋 + st.rerun()으로 반영).
근거: st.session_state로 위젯 값을 제어할 수 있고, st.rerun()은 즉시 재실행하여 화면을 업데이트한다. 
docs.streamlit.io
+1

참고: st.chat_input은 값 주입/기본값 설정이 공식적으로 지원되지 않아(이슈로 남아 있음) 메인 컨테이너에 사용자 정의 텍스트영역 + 버튼을 쓰는 방식이 가장 안전하다. 
GitHub
+2
Streamlit
+2

필요하면 요약 문장 수 슬라이더, 번역 톤(격식/캐주얼) 옵션도 덧붙여줄게.

나의 말:
ㅇㅇ 전체 코드
ChatGPT의 말:
좋아. 수정 반영한 전체 코드다.
변경점: 메인 프롬프트 박스 + 번역 방향(영→한/한→영) 선택 추가, 응답 후 프롬프트 자동 초기화.

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

# ── 메인 프롬프트 박스(텍스트 + 번역 방향 + 액션 버튼) ───────────────────────
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

    trans_dir = st.radio(
        "번역 방향",
        options=("영→한", "한→영"),
        horizontal=True,
        key="__trans_dir"
    )

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None

    def guard_empty() -> bool:
        if not (main_text or "").strip():
            st.warning("프롬프트가 비어 있습니다. 텍스트를 입력하세요.", icon="⚠️")
            return True
        return False

    if c1.button("요약(3줄)", use_container_width=True, key="main_sum"):
        if not guard_empty():
            send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + main_text

    if c2.button("번역", use_container_width=True, key="main_tr"):
        if not guard_empty():
            if trans_dir == "영→한":
                send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + main_text
            else:
                send_prompt = "아래 한국어 문장을 자연스러운 영어로 번역해줘:\n\n" + main_text

    if c3.button("코드 리뷰", use_container_width=True, key="main_rev"):
        if not guard_empty():
            send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + main_text

    if c4.button("그대로 보내기", use_container_width=True, key="main_send"):
        if not guard_empty():
            send_prompt = main_text

# 커스텀 박스에서 눌렀다면 즉시 전송(대화 히스토리에 추가) + 입력창 초기화
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

    # >>> 응답 후 프롬프트 비우기
    st.session_state["__main_task_area"] = ""

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
핵심 근거

번역 방향을 명시적으로 선택해 프롬프트에 반영해야 모델이 원하는 방향으로 동작한다.

입력 위젯 값은 st.session_state["위젯키"]= ""로 초기화 후 st.rerun()으로 즉시 화면 반영 가능.

나의 말:
업로드한 이미지
오류 수정
ChatGPT의 말:
도리, 원인은 st.text_area(key="__main_task_area")를 만든 뒤 같은 런에서 st.session_state["__main_task_area"] = ""로 값을 바꿔서예요. Streamlit은 위젯 생성 이후 동일 키 직접 대입을 금지합니다.
해결: “초기화 플래그”를 세션에 남기고 st.rerun() → 다음 실행에서 위젯 만들기 전에 값을 비웁니다.

아래 파일로 교체하면 끝나요. 변경 핵심은

위쪽 “세션 초기화 영역” 추가

전송 직후 __clear_main 플래그만 켜고 st.rerun() (직접 대입 금지)

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

# ── 세션 준비/초기화(위젯 생성 전) ────────────────────────────────────────────
# 프롬프트 입력 위젯용 키를 미리 준비
if "__main_task_area" not in st.session_state:
    st.session_state["__main_task_area"] = ""
if "__trans_dir" not in st.session_state:
    st.session_state["__trans_dir"] = "영→한"
# 이전 런에서 초기화 플래그가 켜졌다면, 여기서 값을 비우고 플래그 해제
if st.session_state.get("__clear_main"):
    st.session_state["__main_task_area"] = ""
    st.session_state["__clear_main"] = False

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

# ── 메시지 렌더링 ─────────────────────────────────────────────────────────────
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

# ── 메인 프롬프트 박스(텍스트 + 번역 방향 + 액션 버튼) ───────────────────────
st.markdown("<hr/>", unsafe_allow_html=True)
with st.container():
    st.markdown("#### 프롬프트")
    main_text = st.text_area(
        "여기에 텍스트를 붙여넣고 요약/번역/리뷰 버튼을 누르세요.",
        key="__main_task_area",   # 값을 직접 대입하지 말고 키로 관리
        height=160,
        label_visibility="collapsed",
        placeholder="텍스트를 입력하거나 붙여넣기…"
    )

    trans_dir = st.radio(
        "번역 방향",
        options=("영→한", "한→영"),
        horizontal=True,
        key="__trans_dir"
    )

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None

    def guard_empty() -> bool:
        if not (st.session_state["__main_task_area"] or "").strip():
            st.warning("프롬프트가 비어 있습니다. 텍스트를 입력하세요.", icon="⚠️")
            return True
        return False

    if c1.button("요약(3줄)", use_container_width=True, key="main_sum"):
        if not guard_empty():
            send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + st.session_state["__main_task_area"]

    if c2.button("번역", use_container_width=True, key="main_tr"):
        if not guard_empty():
            if st.session_state["__trans_dir"] == "영→한":
                send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + st.session_state["__main_task_area"]
            else:
                send_prompt = "아래 한국어 문장을 자연스러운 영어로 번역해줘:\n\n" + st.session_state["__main_task_area"]

    if c3.button("코드 리뷰", use_container_width=True, key="main_rev"):
        if not guard_empty():
            send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + st.session_state["__main_task_area"]

    if c4.button("그대로 보내기", use_container_width=True, key="main_send"):
        if not guard_empty():
            send_prompt = st.session_state["__main_task_area"]

# 커스텀 박스에서 눌렀다면 즉시 전송(대화 히스토리에 추가) + 다음 런에서 비우기
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

    # 여기서 직접 "__main_task_area"에 대입하지 말 것!
    st.session_state["__clear_main"] = True  # 다음 실행에서 위젯 생성 전에 비움
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
핵심 근거

Streamlit 제약: 위젯 생성 후 같은 런에서 동일 키에 직접 대입하면 예외 발생.

패턴: 플래그(__clear_main) → st.rerun() → 다음 런에서 위젯 생성 전에 값을 초기화.

적용 후에도 문제 있으면 에러 라인 스크린샷 주면 바로 더 손볼게.

나의 말:
Model

gpt-4o-mini
Temperature

Max tokens(응답)

System prompt

이에 대한 설명이 있으면 좋겠다. 롤오버를 하면 설명을 띄워 준다든지 가장 좋은 방법으로 코드 수정해줘.
ChatGPT의 말:
좋은 개선 포인트야 도리!
지금 Model, Temperature, Max tokens, System prompt는 단순한 입력 UI인데, 사용자가 의미를 헷갈릴 수 있어. Streamlit에서 롤오버(hover) 설명은 각 위젯에 help 속성을 달아주는 게 가장 직관적이고 깔끔한 방법이야.

🔧 코드 수정 예시
사이드바 UI 부분을 이렇게 고치면 돼:

with st.sidebar:
    st.subheader("환경 설정")

    key_default = st.session_state.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input(
        "OpenAI API Key",
        value=key_default,
        type="password",
        help="OpenAI API Key를 입력하세요. 세션에 저장되어 새로고침 전까지 유지됩니다."
    )

    model = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini", "gpt-3.5-turbo"],
        index=0,
        help="사용할 OpenAI 모델을 선택합니다.\n- gpt-4o-mini: 빠르고 저렴, 가벼운 작업용\n- gpt-4o: 고품질 응답\n- gpt-4.1-mini, gpt-3.5-turbo: 비용 절감 옵션"
    )

    temperature = st.slider(
        "Temperature",
        0.0, 1.2, 0.7, 0.1,
        help="창의성(랜덤성) 정도를 조절합니다.\n낮으면 일관성↑, 높으면 창의적 응답↑"
    )

    max_tokens = st.slider(
        "Max tokens(응답)",
        256, 4096, 1024, 64,
        help="모델이 한 번에 생성할 수 있는 최대 토큰 수(단어 조각).\n값이 크면 긴 답변 가능하지만 비용/시간↑"
    )

    system_prompt = st.text_area(
        "System prompt",
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 **굵게** 강조합니다.",
        height=100,
        help="모델의 기본 성격과 말투를 정의합니다.\n예: '친절한 선생님처럼 설명해줘'"
    )
📌 결과
마우스를 올리면 각 항목에 대한 설명(tooltip)이 뜸.

설명에는 모델 특징, temperature 의미, max_tokens 역할, system prompt 사용법이 간결히 담김.

가장 단순하면서 유지보수하기 좋은 방식.

👉 도리, 혹시 더 고급스럽게 아이콘 옆에 ℹ️ 버튼을 두고 클릭하면 팝업(예: st.popover)으로 설명을 띄우는 방식도 원해? 아니면 지금처럼 롤오버 툴팁이 제일 깔끔할까?

나의 말:
전체 코드로 다시 줘
ChatGPT의 말:
좋아, 툴팁(롤오버 설명) 추가 + 번역 방향 + 응답 후 입력창 자동 비움 + 세션-세이프 초기화를 모두 반영한 전체 코드야. 그대로 streamlit_app.py에 붙여 넣고 커밋/푸시하면 된다.

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

# ── 세션 준비/초기화(위젯 생성 전) ────────────────────────────────────────────
# 메인 프롬프트와 옵션 기본값을 위젯 생성 전에 준비
if "__main_task_area" not in st.session_state:
    st.session_state["__main_task_area"] = ""
if "__trans_dir" not in st.session_state:
    st.session_state["__trans_dir"] = "영→한"
# 이전 런에서 입력창 초기화 플래그가 켜져 있으면 먼저 비우고 플래그 해제
if st.session_state.get("__clear_main"):
    st.session_state["__main_task_area"] = ""
    st.session_state["__clear_main"] = False

# ── 사이드바(설정/유틸) ───────────────────────────────────────────────────────
with st.sidebar:
    st.subheader("환경 설정")

    key_default = st.session_state.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input(
        "OpenAI API Key",
        value=key_default,
        type="password",
        help="OpenAI API Key를 입력하세요. 세션에 저장되어 새로고침 전까지 유지됩니다."
    )

    model = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini", "gpt-3.5-turbo"],
        index=0,
        help="사용할 OpenAI 모델을 선택합니다.\n- gpt-4o-mini: 빠르고 저렴(가벼운 작업)\n- gpt-4o: 고품질 응답\n- gpt-4.1-mini / gpt-3.5-turbo: 비용 절감 옵션"
    )

    temperature = st.slider(
        "Temperature",
        0.0, 1.2, 0.7, 0.1,
        help="응답의 창의성(랜덤성)을 조절합니다. 낮을수록 일관성↑, 높을수록 다양성/창의성↑"
    )

    max_tokens = st.slider(
        "Max tokens(응답)",
        256, 4096, 1024, 64,
        help="모델이 한 번에 생성할 수 있는 최대 토큰 수(단어 조각). 값이 클수록 긴 답변 가능하지만 비용/시간↑"
    )

    system_prompt = st.text_area(
        "System prompt",
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 **굵게** 강조합니다.",
        height=100,
        help="모델의 기본 성격과 말투를 정의합니다. 예: '친절한 선생님처럼 설명해줘'"
    )

    st.divider()
    col_a, col_b = st.columns(2)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True, help="대화 히스토리를 모두 삭제합니다.")
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True, help="현재까지의 대화 내용을 JSON으로 저장합니다.")

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

# ── 메시지 렌더링 ─────────────────────────────────────────────────────────────
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

# ── 메인 프롬프트 박스(텍스트 + 번역 방향 + 액션 버튼) ───────────────────────
st.markdown("<hr/>", unsafe_allow_html=True)
with st.container():
    st.markdown("#### 프롬프트")
    main_text = st.text_area(
        "여기에 텍스트를 붙여넣고 요약/번역/리뷰 버튼을 누르세요.",
        key="__main_task_area",     # 값을 직접 대입하지 않고 세션 키로 관리
        height=160,
        label_visibility="collapsed",
        placeholder="텍스트를 입력하거나 붙여넣기…"
    )

    trans_dir = st.radio(
        "번역 방향",
        options=("영→한", "한→영"),
        horizontal=True,
        key="__trans_dir",
        help="번역 방향을 선택하세요. 선택에 따라 번역 프롬프트가 자동 구성됩니다."
    )

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None

    def guard_empty() -> bool:
        if not (st.session_state["__main_task_area"] or "").strip():
            st.warning("프롬프트가 비어 있습니다. 텍스트를 입력하세요.", icon="⚠️")
            return True
        return False

    if c1.button("요약(3줄)", use_container_width=True, key="main_sum", help="붙여넣은 텍스트를 3줄로 요약합니다."):
        if not guard_empty():
            send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + st.session_state["__main_task_area"]

    if c2.button("번역", use_container_width=True, key="main_tr", help="선택한 방향(영→한/한→영)으로 번역합니다."):
        if not guard_empty():
            if st.session_state["__trans_dir"] == "영→한":
                send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + st.session_state["__main_task_area"]
            else:
                send_prompt = "아래 한국어 문장을 자연스러운 영어로 번역해줘:\n\n" + st.session_state["__main_task_area"]

    if c3.button("코드 리뷰", use_container_width=True, key="main_rev", help="코드 품질/취약점/가독성을 리뷰하고 수정 예시를 제시합니다."):
        if not guard_empty():
            send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + st.session_state["__main_task_area"]

    if c4.button("그대로 보내기", use_container_width=True, key="main_send", help="붙여넣은 텍스트를 그대로 전송합니다."):
        if not guard_empty():
            send_prompt = st.session_state["__main_task_area"]

# 커스텀 박스에서 눌렀다면 즉시 전송(대화 히스토리에 추가) + 다음 런에서 입력창 비우기
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

    # 다음 실행에서 텍스트박스를 비우도록 플래그만 설정
    st.session_state["__clear_main"] = True
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
포인트

**각 위젯에 help**를 달아 롤오버 툴팁 제공.

번역 방향 라디오(영→한/한→영) 반영.

응답 후 입력창 비움: 같은 런에서 값 대입 금지 → __clear_main 플래그 + st.rerun() 패턴으로 안정 처리.

나의 말:
업로드한 이미지
그대로 보내기를 하면 기본 프롬프트에서의 답이 나와야 하는데 위에서 진행했던  결과가 이어지면서 번역이 되거나 요약이 되어서 나온다. 이전 실행에 영향을 받지 않도록 수정해줘.
ChatGPT의 말:

25s 동안 생각함
좋아. “그대로 보내기”가 이전 실행(요약/번역) 영향 없이 동작하도록 전체 코드를 손봤어.

핵심 수정
컨텍스트 모드 추가: 대화 연속 / 이전 대화 무시(기본)
→ 버튼으로 보낼 때, 기본값은 이전 대화 무시라서 이전 요약/번역 지시가 새 요청에 끼어들지 않음.

“그대로 보내기”는 기본적으로 이전 대화 무시 모드를 사용(원하면 대화 연속으로 바꿔 가능).

기존의 툴팁, 번역 방향, 응답 후 입력창 자동 비움, 세션-세이프 초기화 유지.

아래 파일로 교체하세요.

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

# ── 세션 준비/초기화(위젯 생성 전) ────────────────────────────────────────────
if "__main_task_area" not in st.session_state:
    st.session_state["__main_task_area"] = ""
if "__trans_dir" not in st.session_state:
    st.session_state["__trans_dir"] = "영→한"
# 새로 추가: 컨텍스트 모드 (기본=이전 대화 무시)
if "__ctx_mode" not in st.session_state:
    st.session_state["__ctx_mode"] = "이전 대화 무시"  # 또는 "대화 연속"
# 이전 런에서 입력창 초기화 플래그가 켜져 있으면 먼저 비우고 플래그 해제
if st.session_state.get("__clear_main"):
    st.session_state["__main_task_area"] = ""
    st.session_state["__clear_main"] = False

# ── 사이드바(설정/유틸) ───────────────────────────────────────────────────────
with st.sidebar:
    st.subheader("환경 설정")

    key_default = st.session_state.get("OPENAI_API_KEY", "")
    api_key_input = st.text_input(
        "OpenAI API Key",
        value=key_default,
        type="password",
        help="OpenAI API Key를 입력하세요. 세션에 저장되어 새로고침 전까지 유지됩니다."
    )

    model = st.selectbox(
        "Model",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini", "gpt-3.5-turbo"],
        index=0,
        help="사용할 OpenAI 모델을 선택합니다.\n- gpt-4o-mini: 빠르고 저렴(가벼운 작업)\n- gpt-4o: 고품질 응답\n- gpt-4.1-mini / gpt-3.5-turbo: 비용 절감 옵션"
    )

    temperature = st.slider(
        "Temperature",
        0.0, 1.2, 0.7, 0.1,
        help="응답의 창의성(랜덤성)을 조절합니다. 낮을수록 일관성↑, 높을수록 다양성/창의성↑"
    )

    max_tokens = st.slider(
        "Max tokens(응답)",
        256, 4096, 1024, 64,
        help="모델이 한 번에 생성할 수 있는 최대 토큰 수(단어 조각). 값이 클수록 긴 답변 가능하지만 비용/시간↑"
    )

    system_prompt = st.text_area(
        "System prompt",
        value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 **굵게** 강조합니다.",
        height=100,
        help="모델의 기본 성격과 말투를 정의합니다. 예: '친절한 선생님처럼 설명해줘'"
    )

    st.divider()
    col_a, col_b = st.columns(2)
    clear_clicked = col_a.button("대화 초기화", use_container_width=True, help="대화 히스토리를 모두 삭제합니다.")
    download_clicked = col_b.button("내려받기(JSON)", use_container_width=True, help="현재까지의 대화 내용을 JSON으로 저장합니다.")

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

# ── 메시지 렌더링 ─────────────────────────────────────────────────────────────
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

# ── 메인 프롬프트 박스(텍스트 + 번역 방향 + 컨텍스트 모드 + 액션 버튼) ────────
st.markdown("<hr/>", unsafe_allow_html=True)
with st.container():
    st.markdown("#### 프롬프트")
    main_text = st.text_area(
        "여기에 텍스트를 붙여넣고 요약/번역/리뷰/그대로 보내기 버튼을 누르세요.",
        key="__main_task_area",
        height=160,
        label_visibility="collapsed",
        placeholder="텍스트를 입력하거나 붙여넣기…"
    )

    cols = st.columns([1,1,1])
    with cols[0]:
        trans_dir = st.radio(
            "번역 방향",
            options=("영→한", "한→영"),
            horizontal=True,
            key="__trans_dir",
            help="번역 방향을 선택하세요. 선택에 따라 번역 프롬프트가 자동 구성됩니다."
        )
    with cols[1]:
        ctx_mode = st.radio(
            "컨텍스트",
            options=("대화 연속", "이전 대화 무시"),
            index=1,  # 기본값: 이전 대화 무시
            key="__ctx_mode",
            help="대화 연속: 이전 대화 맥락을 함께 보냄\n이전 대화 무시: 지금 입력만 단독으로 보냄"
        )
    with cols[2]:
        st.write("")  # spacing

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    send_prompt = None
    action = None  # 'summary' | 'translate' | 'review' | 'send_raw'

    def guard_empty() -> bool:
        if not (st.session_state["__main_task_area"] or "").strip():
            st.warning("프롬프트가 비어 있습니다. 텍스트를 입력하세요.", icon="⚠️")
            return True
        return False

    if c1.button("요약(3줄)", use_container_width=True, key="main_sum",
                 help="붙여넣은 텍스트를 3줄로 요약합니다."):
        if not guard_empty():
            send_prompt = "아래 텍스트를 3줄로 요약해줘:\n\n" + st.session_state["__main_task_area"]
            action = "summary"

    if c2.button("번역", use_container_width=True, key="main_tr",
                 help="선택한 방향(영→한/한→영)으로 번역합니다."):
        if not guard_empty():
            if st.session_state["__trans_dir"] == "영→한":
                send_prompt = "아래 영어 문장을 자연스러운 한국어로 번역해줘:\n\n" + st.session_state["__main_task_area"]
            else:
                send_prompt = "아래 한국어 문장을 자연스러운 영어로 번역해줘:\n\n" + st.session_state["__main_task_area"]
            action = "translate"

    if c3.button("코드 리뷰", use_container_width=True, key="main_rev",
                 help="코드 품질/취약점/가독성을 리뷰하고 수정 예시를 제시합니다."):
        if not guard_empty():
            send_prompt = "아래 코드에서 취약점/가독성/성능을 리뷰하고 수정 예시를 제시해줘:\n\n" + st.session_state["__main_task_area"]
            action = "review"

    if c4.button("그대로 보내기", use_container_width=True, key="main_send",
                 help="붙여넣은 텍스트를 가공 없이 그대로 전송합니다. (기본: 이전 대화 무시)"):
        if not guard_empty():
            send_prompt = st.session_state["__main_task_area"]
            action = "send_raw"
            # 그대로 보내기는 기본적으로 맥락을 무시하도록 강제할 수도 있음:
            # ctx_mode = "이전 대화 무시"
            # st.session_state["__ctx_mode"] = "이전 대화 무시"

# 커스텀 박스에서 눌렀다면 즉시 전송 + 다음 런에서 입력창 비우기
if send_prompt and client:
    # === 컨텍스트 선택 적용 ===
    history: List[Dict[str, str]] = []
    if system_prompt.strip():
        history.append({"role": "system", "content": system_prompt.strip()})

    use_history = (st.session_state["__ctx_mode"] == "대화 연속")
    # "그대로 보내기"는 기본적으로 이전 대화 무시를 권장
    if action == "send_raw" and st.session_state["__ctx_mode"] != "대화 연속":
        use_history = False

    if use_history:
        history.extend(st.session_state.messages)

    # 사용자 메시지 추가
    user_msg = {"role": "user", "content": send_prompt}
    history.append(user_msg)

    # 렌더 + 세션 저장
    render_message("user", send_prompt)
    st.session_state.messages.append({**user_msg, "time": datetime.now().strftime("%H:%M")})

    # 스트리밍 응답
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

    # 다음 실행에서 텍스트박스를 비우도록 플래그만 설정
    st.session_state["__clear_main"] = True
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
이제 그대로 보내기를 눌러도 이전 요약/번역 맥락에 끌려가지 않고, 컨텍스트 라디오로 필요 시만 대화 연속을 선택해 쓸 수 있어.

나의 말:
** 이게 안 붙게 수정해줘 영 가독성이 떨어지네
ChatGPT의 말:

27s 동안 생각함
오케이. 출력에서 **가 아예 보이지 않도록 스트리밍 단계에서 마크다운 굵게/이탤릭 표식을 제거해 버리게 수정하자. (이러면 모델이 **굵게**를 써도 UI에는 깔끔한 일반 텍스트로 표시됨)

변경 요점
마크다운 서식 제거 함수 추가(strip_md).

스트리밍 출력 경로를 강제 커스텀 렌더링으로 사용해, 토큰을 누적하면서 항상 서식 제거 후 표시.

기본 시스템 프롬프트 예시에서 ** 제거.

아래 패치만 적용하면 돼. (파일 전체 교체 필요 없음)

# 상단 import 근처에 추가
import re
# 스트리밍 위에 유틸 추가
USE_NATIVE_STREAM = False  # True면 st.write_stream 사용, False면 커스텀 렌더링(서식 제거)

def strip_md(s: str) -> str:
    """굵게/이탤릭 마크다운(**, *, __, _)을 제거"""
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s, flags=re.S)  # **bold**
    s = re.sub(r"\*(.*?)\*", r"\1", s)                  # *italic*
    s = re.sub(r"__(.*?)__", r"\1", s, flags=re.S)      # __bold__
    s = re.sub(r"_(.*?)_", r"\1", s)                    # _italic_
    s = s.replace("**", "")  # 비정상 잔여 처리
    return s
# 사이드바의 system_prompt 기본값 문자열에서 ** 제거
system_prompt = st.text_area(
    "System prompt",
    value="당신은 전문적이면서 간결한 한국어 어시스턴트입니다. 핵심은 굵게 강조하지 말고, 명확한 bullet로만 정리합니다.",
    height=100,
    help="모델의 기본 성격과 말투를 정의합니다. 예: '친절한 선생님처럼 설명해줘'"
)
# write_stream_safe 교체
def write_stream_safe(gen: Generator[str, None, None]) -> str:
    """
    st.write_stream 대신 커스텀 렌더링을 기본으로 사용해서
    ** 등 마크다운 서식을 제거한 텍스트를 실시간 표시/반환.
    """
    if USE_NATIVE_STREAM and hasattr(st, "write_stream"):
        # 네이티브 스트림을 쓰고 싶으면 True로 바꿔 사용 (서식 제거 안 됨)
        return st.write_stream(gen)

    ph = st.empty()
    acc = []
    for tok in gen:
        acc.append(tok)
        # 누적 문자열을 서식 제거하고 출력
        safe_text = strip_md("".join(acc))
        ph.markdown(
            f'<div class="msg bot"><div class="meta">assistant · {datetime.now():%H:%M}</div>{safe_text}</div>',
            unsafe_allow_html=True
        )
    return strip_md("".join(acc))
참고: 우리는 write_stream_safe(...)의 반환값(최종 텍스트)도 서식 제거된 것을 돌려주므로, 세션 히스토리에 저장되는 내용 역시 **가 없습니다. 과거 대화에 남아 있던 **는 그대로지만, 이후 응답부터는 전부 깔끔한 일반 텍스트로 나옵니다.

필요하면 strip_md에 목록/헤딩 제거까지 확대해 줄 수도 있어. 지금은 굵게/이탤릭만 제거해서 본문 가독성만 손봤어.

나의 말:
전체 코드
ChatGPT의 말:
좋아 도리, 요청대로 전체 코드를 다시 정리했어.
이번 버전은 ** 같은 마크다운 서식 제거, 툴팁(hover 설명), 프롬프트 입력 후 자동 비움, 컨텍스트(대화 연속/이전 대화 무시), 그대로 보내기 오류 수정까지 모두 반영돼.

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
이제 결과에서 **가 완전히 사라져서 가독성이 좋아지고, 그대로 보내기도 이전 실행에 안 끌려.
도리, 혹시 결과를 **순수 텍스트(st.text)**로만 뿌리길 원해? (마크다운 태그도 완전히 제거)



선택된 파일 없음선택된 파일 없음
ChatGPT는 실수를 할 수 있습니다. 중요한 정보는 재차 확인하세요.
