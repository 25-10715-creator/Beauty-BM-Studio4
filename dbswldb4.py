import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="Beauty BM Studio",
    page_icon="💄",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("💄 Beauty BM Studio")
st.markdown("색조 화장품 브랜드 기획자를 위한 분석 앱")

# -----------------------------
# 샘플 데이터
# -----------------------------
products = pd.DataFrame({
    "브랜드": ["Rom&nd", "3CE", "Hince", "Clio"],
    "제품": ["쥬시 틴트", "벨벳 립", "글로우 립밤", "킬커버 쿠션"],
    "가격": [13000, 17000, 18000, 32000],
    "평점": [4.7, 4.5, 4.8, 4.6],
    "판매량": [5400, 4300, 3900, 6100]
})

# -----------------------------
# 사이드바 메뉴
# -----------------------------
menu = st.sidebar.selectbox(
    "메뉴 선택",
    [
        "BM 대시보드",
        "경쟁 브랜드 분석",
        "퍼스널 컬러 추천"
    ]
)

# -----------------------------
# BM 대시보드
# -----------------------------
if menu == "BM 대시보드":

    st.header("📊 BM 대시보드")

    col1, col2, col3 = st.columns(3)

    col1.metric("총 판매량", "19,700", "+15%")
    col2.metric("평균 평점", "4.65", "+0.2")
    col3.metric("신제품 수", "4", "+1")

    st.markdown("---")

    st.subheader("브랜드 판매량 분석")

    fig = px.bar(
        products,
        x="브랜드",
        y="판매량",
        color="브랜드",
        title="브랜드별 판매량"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(products, use_container_width=True)

# -----------------------------
# 경쟁 브랜드 분석
# -----------------------------
elif menu == "경쟁 브랜드 분석":

    st.header("📈 경쟁 브랜드 분석")

    brand = st.selectbox(
        "브랜드 선택",
        products["브랜드"]
    )

    filtered = products[
        products["브랜드"] == brand
    ]

    st.dataframe(filtered, use_container_width=True)

    scatter = px.scatter(
        products,
        x="가격",
        y="평점",
        size="판매량",
        color="브랜드",
        hover_name="제품",
        title="브랜드 포지셔닝"
    )

    st.plotly_chart(scatter, use_container_width=True)

# -----------------------------
# 퍼스널 컬러 추천
# -----------------------------
elif menu == "퍼스널 컬러 추천":

    st.header("🎨 퍼스널 컬러 추천")

    skin = st.selectbox(
        "피부톤 선택",
        ["봄 웜", "여름 쿨", "가을 웜", "겨울 쿨"]
    )

    color_map = {
        "봄 웜": ["코랄", "피치", "살몬 핑크"],
        "여름 쿨": ["로즈", "모브", "쿨 핑크"],
        "가을 웜": ["브릭", "테라코타", "브라운 레드"],
        "겨울 쿨": ["버건디", "체리 레드", "플럼"]
    }

    recommended = color_map[skin]

    st.success(
        f"{skin} 추천 컬러: {', '.join(recommended)}"
    )

    color_df = pd.DataFrame({
        "추천 컬러": recommended,
        "트렌드 점수": [92, 88, 85]
    })

    color_chart = px.bar(
        color_df,
        x="추천 컬러",
        y="트렌드 점수",
        color="추천 컬러",
        title="퍼스널 컬러 트렌드 분석"
    )

    st.plotly_chart(
        color_chart,
        use_container_width=True
    )
