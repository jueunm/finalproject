import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# 🎯 타이틀
# ------------------------

st.set_page_config(page_title="📅 2024년 모기 개체수 예측", page_icon="🔮")
st.title("🔮 2024년 월별 모기 개체수 예측")

# ------------------------
# 📁 데이터 로드
# ------------------------

url = "연도별_월별_모기_개체수_합계.csv"
df = pd.read_csv(url, header=1, encoding='cp949')
df.columns = ['연도', '월', '모기계']
df['연도'] = df['연도'].astype(int)
df['월'] = df['월'].astype(int)
df['모기계'] = df['모기계'].astype(int)

# ------------------------
# 📅 최근 N년 평균
# ------------------------

N = st.slider("최근 몇 년의 데이터를 평균낼까요?", 1, 10, 5)

recent_years = df['연도'].max() - N + 1
recent_df = df[df['연도'] >= recent_years]

monthly_forecast = recent_df.groupby('월')['모기계'].mean().reset_index()
monthly_forecast['모기계'] = monthly_forecast['모기계'].round().astype(int)
monthly_forecast['연도'] = 2024

# ------------------------
# 📈 시각화 (실제 vs 예측)
# ------------------------

# 실제 데이터 (마지막 N년)
plot_df = pd.concat([
    df[df['연도'] >= recent_years],
    monthly_forecast
])

fig = px.line(
    plot_df,
    x='월',
    y='모기계',
    color='연도',
    markers=True,
    title=f"📅 최근 {N}년 데이터 기반 2024년 월별 모기 개체수 예측",
    labels={
        '월': '월',
        '모기계': '모기 개체수',
        '연도': '연도'
    },
    template='plotly_white'
)

fig.update_layout(
    xaxis=dict(tickmode='linear', dtick=1),
    yaxis=dict(title='모기 개체수'),
    hovermode='x unified',
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# 🔍 표 보기
# ------------------------

with st.expander("📋 예측 값 확인하기"):
    st.dataframe(monthly_forecast)

st.success(f"✅ 2024년 예측은 최근 {N}년간의 월별 평균값으로 계산되었습니다.")
