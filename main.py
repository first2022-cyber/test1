import streamlit as st
import random

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="🐣",
    layout="centered",
)

# 따뜻한 크림·노란색 테마
st.markdown(
    """
    <style>
    .stApp {
        background: #fffdf5;
        color: #49391f;
    }
    h1, h2, h3 {
        color: #d88908 !important;
    }
    .intro {
        background: #fff3cc;
        border: 2px solid #f4d77c;
        border-radius: 20px;
        padding: 18px 22px;
        font-size: 1.15rem;
        line-height: 1.7;
        margin-bottom: 18px;
    }
    .pokemon-card {
        background: #fff8e6;
        border: 2px solid #f3dfaa;
        border-radius: 24px;
        padding: 24px;
        text-align: center;
        margin-top: 18px;
    }
    .pokemon-name {
        color: #d88908;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .pokemon-en {
        color: #806a43;
        font-size: 1.1rem;
        margin-bottom: 14px;
    }
    .info-label {
        color: #9a6500;
        font-weight: 800;
        font-size: 1.1rem;
    }
    .info-text {
        font-size: 1.08rem;
        line-height: 1.8;
    }
    div[data-baseweb="select"] {
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

POKEMON = {
    "ENFP": {
        "ko": "피카츄", "en": "Pikachu", "emoji": "⚡",
        "type": "전기",
        "trait": "호기심이 많고 활발하며 주변을 밝게 만드는 포켓몬",
        "reason": "새로운 경험을 즐기고 사람들과 어울리는 ENFP와 피카츄는 에너지가 잘 통하는 단짝이에요.\\n함께라면 평범한 하루도 신나는 모험이 될 거예요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    },
    "ENFJ": {
        "ko": "푸린", "en": "Jigglypuff", "emoji": "🎤",
        "type": "노말·페어리",
        "trait": "노래를 좋아하고 친구들의 기분을 살피는 포켓몬",
        "reason": "다른 사람을 챙기는 ENFJ에게 푸린은 마음을 편안하게 해 주는 친구예요.\\n따뜻한 배려와 즐거운 노래로 서로에게 힘이 되어 줄 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
    },
    "ENTP": {
        "ko": "파오리", "en": "Farfetch'd", "emoji": "🦆",
        "type": "노말·비행",
        "trait": "자신만의 방식으로 재치 있게 문제를 해결하는 포켓몬",
        "reason": "기발한 생각을 즐기는 ENTP와 파오리는 늘 새로운 방법을 찾아낼 것 같아요.\\n서로의 아이디어를 주고받으며 지루할 틈 없는 모험을 펼칠 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/83.png",
    },
    "ENTJ": {
        "ko": "갸라도스", "en": "Gyarados", "emoji": "🌊",
        "type": "물·비행",
        "trait": "강력한 힘과 추진력을 가진 포켓몬",
        "reason": "목표를 세우고 앞장서는 ENTJ와 강력한 갸라도스는 추진력이 잘 어울려요.\\n큰 도전 앞에서도 함께 용기를 내고 끝까지 나아갈 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png",
    },
    "ESFP": {
        "ko": "이상해꽃", "en": "Venusaur", "emoji": "🌻",
        "type": "풀·독",
        "trait": "햇살과 자연을 떠올리게 하는 든든한 포켓몬",
        "reason": "밝고 활동적인 ESFP에게 이상해꽃은 즐거운 시간을 함께 보내기 좋은 친구예요.\\n함께 자연을 탐험하며 주변의 작은 즐거움도 발견할 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
    },
    "ESFJ": {
        "ko": "럭키", "en": "Chansey", "emoji": "💗",
        "type": "노말",
        "trait": "다친 포켓몬을 돌보고 행복을 나누는 포켓몬",
        "reason": "주변 사람을 잘 챙기는 ESFJ와 럭키는 다정함이라는 공통점이 있어요.\\n서로를 보살피고 좋은 기운을 나누는 포근한 단짝이 될 거예요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
    },
    "ESTP": {
        "ko": "리자몽", "en": "Charizard", "emoji": "🔥",
        "type": "불꽃·비행",
        "trait": "도전을 두려워하지 않고 하늘을 힘차게 나는 포켓몬",
        "reason": "직접 경험하고 도전하는 것을 좋아하는 ESTP와 리자몽은 모험심이 닮았어요.\\n새로운 장소를 찾아다니며 짜릿한 경험을 함께할 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
    },
    "ESTJ": {
        "ko": "코뿌리", "en": "Rhydon", "emoji": "🪨",
        "type": "땅·바위",
        "trait": "튼튼한 몸과 강한 힘으로 앞길을 개척하는 포켓몬",
        "reason": "책임감 있고 실행력이 좋은 ESTJ와 코뿌리는 믿음직한 팀을 만들어요.\\n계획을 세우고 차근차근 목표를 이루는 과정에서 서로에게 든든한 힘이 될 거예요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png",
    },
    "INFP": {
        "ko": "이브이", "en": "Eevee", "emoji": "🌸",
        "type": "노말",
        "trait": "다양한 가능성을 품고 여러 모습으로 성장할 수 있는 포켓몬",
        "reason": "상상력이 풍부하고 자신만의 가치를 소중히 여기는 INFP와 이브이는 닮은 점이 많아요.\\n서로의 개성을 존중하며 함께 성장하는 단짝이 될 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
    },
    "INFJ": {
        "ko": "가디안", "en": "Gardevoir", "emoji": "🌙",
        "type": "에스퍼·페어리",
        "trait": "소중한 사람을 지키려는 마음이 강한 포켓몬",
        "reason": "깊이 공감하고 의미 있는 관계를 소중히 여기는 INFJ에게 가디안은 잘 어울려요.\\n말하지 않아도 마음을 헤아리고 서로를 지켜 주는 친구가 될 거예요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png",
    },
    "INTP": {
        "ko": "폴리곤", "en": "Porygon", "emoji": "🧩",
        "type": "노말",
        "trait": "디지털 공간과 관련된 독특한 포켓몬",
        "reason": "원리를 탐구하고 논리적으로 생각하는 INTP와 폴리곤은 호기심의 방향이 비슷해요.\\n함께 새로운 규칙과 신기한 현상을 발견하는 탐구 파트너가 될 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png",
    },
    "INTJ": {
        "ko": "뮤츠", "en": "Mewtwo", "emoji": "🔮",
        "type": "에스퍼",
        "trait": "뛰어난 지능과 강한 집중력을 지닌 포켓몬",
        "reason": "전략적으로 생각하고 장기적인 목표를 세우는 INTJ와 뮤츠는 지적인 분위기가 잘 어울려요.\\n어려운 문제도 차분히 분석하며 함께 해결해 나갈 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
    },
    "ISFP": {
        "ko": "치코리타", "en": "Chikorita", "emoji": "🌿",
        "type": "풀",
        "trait": "온화하고 주변의 분위기를 편안하게 만드는 포켓몬",
        "reason": "감각적이고 자신의 속도로 세상을 느끼는 ISFP에게 치코리타는 편안한 친구예요.\\n조용히 산책하고 작은 아름다움을 발견하며 함께 시간을 보낼 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/152.png",
    },
    "ISFJ": {
        "ko": "럭키", "en": "Chansey", "emoji": "💗",
        "type": "노말",
        "trait": "주변을 세심하게 살피고 돌보는 포켓몬",
        "reason": "성실하고 따뜻하게 주변을 챙기는 ISFJ와 럭키는 배려심이 잘 맞아요.\\n서로의 하루를 보살피며 편안하고 믿음직한 우정을 쌓을 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
    },
    "ISTP": {
        "ko": "팬텀", "en": "Gengar", "emoji": "👻",
        "type": "고스트·독",
        "trait": "장난기 있고 예상 밖의 행동으로 놀라움을 주는 포켓몬",
        "reason": "직접 만지고 실험하며 문제를 해결하는 ISTP와 팬텀은 독특한 호흡을 보여 줄 거예요.\\n복잡한 상황에서도 침착하게 방법을 찾아내고 유쾌한 장난도 함께 즐길 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
    },
    "ISTJ": {
        "ko": "거북왕", "en": "Blastoise", "emoji": "🐢",
        "type": "물",
        "trait": "튼튼한 등껍질과 안정적인 힘을 지닌 포켓몬",
        "reason": "차근차근 책임을 다하는 ISTJ와 거북왕은 믿음직한 파트너가 될 수 있어요.\\n꾸준히 연습하고 약속을 지키며 목표를 함께 이루어 나갈 수 있어요.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
    },
}

st.title("🐣 MBTI로 내 단짝 포켓몬 찾기")
st.markdown(
    '<div class="intro">내 MBTI를 선택하면 나와 잘 어울리는 포켓몬을 찾아드려요!<br>'
    '어떤 포켓몬이 기다리고 있을까요? ✨</div>',
    unsafe_allow_html=True,
)

mbti_types = [
    "ENFP", "ENFJ", "ENTP", "ENTJ",
    "ESFP", "ESFJ", "ESTP", "ESTJ",
    "INFP", "INFJ", "INTP", "INTJ",
    "ISFP", "ISFJ", "ISTP", "ISTJ",
]

selected_mbti = st.selectbox(
    "🌟 내 MBTI를 선택해 주세요",
    mbti_types,
    index=None,
    placeholder="MBTI를 선택하세요",
)

if selected_mbti:
    pokemon = POKEMON[selected_mbti]

    st.balloons()
    st.markdown(
        f"""
        <div class="pokemon-card">
          <div style="font-size:1.15rem;font-weight:800;color:#9a6500;">
            🎉 축하해요! 당신의 단짝 포켓몬을 찾았어요!
          </div>
          <div style="font-size:4rem;margin-top:10px;">{pokemon['emoji']}</div>
          <div class="pokemon-name">{pokemon['ko']}</div>
          <div class="pokemon-en">({pokemon['en']})</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 포켓몬 이미지는 인터넷에서 가져옵니다.
    st.image(pokemon["image"], width=220)

    st.markdown(
        f"""
        <div class="pokemon-card" style="text-align:left;">
          <p><span class="info-label">🔖 타입</span><br>
          <span class="info-text">{pokemon['type']}</span></p>
          <p><span class="info-label">✨ 특징</span><br>
          <span class="info-text">{pokemon['trait']}</span></p>
          <p><span class="info-label">💛 왜 잘 어울릴까요?</span><br>
          <span class="info-text">{pokemon['reason'].replace(chr(10), '<br>')}</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
