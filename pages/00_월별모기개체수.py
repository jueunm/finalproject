import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# 🎉 페이지 타이틀 & 설명
# ------------------------

st.set_page_config(
    page_title="🦟 월별 평균 모기 개체수 분석",
    page_icon="🦟",
    layout="wide"
)

st.title("📊✨ 월별 평균 모기 개체수 분석(2008~2023) ✨🦟")
st.markdown(
    """
    ## 📅 월별 평균 모기 트렌드
    모기 개체수는 계절과 온도에 따라 어떻게 변할까요?  
    모든 연도의 데이터를 모아 **월별 평균 모기 개체수**를 확인해보세요! 🌙🌞

    ---
    """
)

# ------------------------
# 📁 데이터 불러오기
# ------------------------

url = "연도별_월별_모기_개체수_합계.csv"  # 👉 깃허브 raw URL로 변경 가능
df = pd.read_csv(url, header=1, encoding='cp949')

# 컬럼명 & 타입 정리
df.columns = ['연도', '월', '모기계']
df['연도'] = df['연도'].astype(int)
df['월'] = df['월'].astype(int)
df['모기계'] = df['모기계'].astype(int)

# ------------------------
# 🧮 월별 평균 계산
# ------------------------

monthly_avg = df.groupby('월')['모기계'].mean().reset_index()
monthly_avg['모기계'] = monthly_avg['모기계'].round().astype(int)

# ------------------------
# 📈 Plotly 라인 그래프
# ------------------------

fig = px.line(
    monthly_avg,
    x='월',
    y='모기계',
    markers=True,
    title="🌿🦟 월별 평균 모기 개체수 변화 🗓️",
    labels={
        '월': '월',
        '모기계': '평균 모기 개체수'
    },
    template='plotly_white'
)

fig.update_layout(
    xaxis=dict(tickmode='linear', dtick=1),
    yaxis=dict(title='평균 모기 개체수'),
    hovermode='x unified',
    title_x=0.5
)

# ------------------------
# ✅ Streamlit 출력
# ------------------------

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# 📊 데이터프레임 보기
# ------------------------

with st.expander("🔍 📋 월별 평균 모기 개체수 표 보기"):
    st.dataframe(monthly_avg.style.highlight_max(axis=0, color='lightgreen'))

# ------------------------
# ℹ️ 추가 정보
# ------------------------

st.info("💡 **TIP:** 봄과 여름철에 모기 개체수가 증가하므로 예방에 주의하세요! 🧴🦟")
