import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# MBTI별 단짝 포켓몬 데이터
# 이미지 주소는 PokeAPI sprites 저장소의 공식 아트워크 파일을 사용합니다.
# 앱 자체는 외부 API를 호출하지 않으며, 이미지 표시 때만 인터넷이 필요합니다.
# ------------------------------------------------------------
POKEMON = {
    "ENFP": {
        "name": "피카츄", "english": "Pikachu", "id": 25,
        "type": "전기", "type_emoji": "⚡",
        "feature": "호기심이 많고 에너지가 넘치는 분위기 메이커",
        "why": "새로운 일을 보면 함께 뛰어들어 줄 든든한 모험 친구예요.\\n밝은 에너지로 아이디어를 더 신나게 펼쳐 줘요.",
        "color": "#F6C94D",
    },
    "ENFJ": {
        "name": "푸린", "english": "Jigglypuff", "id": 39,
        "type": "노말 · 페어리", "type_emoji": "🎤",
        "feature": "다정하고 표현력이 풍부한 작은 가수",
        "why": "친구들의 기분을 살피고 따뜻하게 응원해 줘요.\\n함께 노래하고 이야기하다 보면 모두가 편안해져요.",
        "color": "#F3A8C8",
    },
    "ENTP": {
        "name": "파오리", "english": "Farfetch'd", "id": 83,
        "type": "노말 · 비행", "type_emoji": "🦆",
        "feature": "자기만의 도구를 활용하는 재치 있는 전략가",
        "why": "엉뚱한 아이디어도 재미있는 도전으로 바꿔 줘요.\\n서로 생각을 주고받으며 새로운 방법을 찾아낼 수 있어요.",
        "color": "#B6D5A8",
    },
    "ENTJ": {
        "name": "갸라도스", "english": "Gyarados", "id": 130,
        "type": "물 · 비행", "type_emoji": "🌊",
        "feature": "강한 추진력과 압도적인 존재감을 가진 포켓몬",
        "why": "목표를 정하면 힘차게 나아가는 모습을 닮았어요.\\n큰 계획도 용기 있게 시작하도록 서로 북돋아 줘요.",
        "color": "#8CC8E8",
    },
    "ESFP": {
        "name": "이상해꽃", "english": "Venusaur", "id": 3,
        "type": "풀 · 독", "type_emoji": "🌻",
        "feature": "햇살과 자연의 기운을 품은 든든한 친구",
        "why": "함께하는 시간을 풍성하고 즐겁게 만들어 줘요.\\n활동적인 하루에도 편안히 쉴 수 있는 안정감을 더해요.",
        "color": "#A8D5A0",
    },
    "ESFJ": {
        "name": "럭키", "english": "Chansey", "id": 113,
        "type": "노말", "type_emoji": "💗",
        "feature": "다른 이를 돌보는 것을 좋아하는 상냥한 포켓몬",
        "why": "작은 변화도 알아차리고 먼저 챙겨 주는 모습이 잘 어울려요.\\n서로를 응원하며 따뜻한 팀워크를 만들 수 있어요.",
        "color": "#F6B7C9",
    },
    "ESTP": {
        "name": "리자몽", "english": "Charizard", "id": 6,
        "type": "불꽃 · 비행", "type_emoji": "🔥",
        "feature": "모험을 좋아하고 행동력이 뛰어난 포켓몬",
        "why": "망설이기보다 직접 경험하며 배우는 성향과 잘 맞아요.\\n새로운 장소와 도전을 함께 누비는 콤비가 될 수 있어요.",
        "color": "#F3A36D",
    },
    "ESTJ": {
        "name": "코뿌리", "english": "Rhydon", "id": 112,
        "type": "땅 · 바위", "type_emoji": "🪨",
        "feature": "튼튼한 몸과 힘으로 앞장서는 믿음직한 포켓몬",
        "why": "맡은 일을 책임감 있게 해내는 점이 서로 닮았어요.\\n계획을 세우고 차근차근 목표를 이루는 팀이 되어 줘요.",
        "color": "#C5B8A5",
    },
    "INFP": {
        "name": "이브이", "english": "Eevee", "id": 133,
        "type": "노말", "type_emoji": "🌸",
        "feature": "가능성이 많고 마음이 따뜻한 포켓몬",
        "why": "자신만의 속도와 개성을 소중히 여기는 모습이 닮았어요.\\n편안한 곁에서 상상력과 가능성을 마음껏 키울 수 있어요.",
        "color": "#D9B28C",
    },
    "INFJ": {
        "name": "가디안", "english": "Gardevoir", "id": 282,
        "type": "에스퍼 · 페어리", "type_emoji": "🌙",
        "feature": "소중한 이를 지키려는 마음이 깊은 포켓몬",
        "why": "말하지 않은 마음까지 헤아리려는 다정함이 잘 어울려요.\\n복잡한 생각을 차분히 나누고 서로에게 힘이 되어 줘요.",
        "color": "#B9C6E8",
    },
    "INTP": {
        "name": "폴리곤", "english": "Porygon", "id": 137,
        "type": "노말", "type_emoji": "🧩",
        "feature": "디지털 공간에서 활동하는 독특하고 논리적인 포켓몬",
        "why": "궁금한 것을 깊이 파고들며 원리를 찾는 성향과 잘 맞아요.\\n함께 관찰하고 가설을 세우며 재미있는 답을 찾아봐요.",
        "color": "#A9C9E8",
    },
    "INTJ": {
        "name": "뮤츠", "english": "Mewtwo", "id": 150,
        "type": "에스퍼", "type_emoji": "🔮",
        "feature": "뛰어난 지능과 전략적인 사고를 지닌 포켓몬",
