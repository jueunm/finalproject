import streamlit as st
import pandas as pd
import plotly.express as px

# 1️⃣ 제목
st.title("대한민국 연도별·월별 모기 개체수 변화🦟")

# 2️⃣ 깃허브 raw URL 또는 로컬 파일 경로
url = "year_month_mosquito_sum.csv"  # 필요 시 깃허브 raw URL로 변경

# ✅ encoding='cp949' 추가
df = pd.read_csv(url, header=1, encoding='cp949')

# 3️⃣ 컬럼명 설정
df.columns = ['연도', '월', '모기계']

# 4️⃣ 데이터 타입 변환
df['연도'] = df['연도'].astype(int)
df['월'] = df['월'].astype(int)
df['모기계'] = df['모기계'].astype(int)

# 5️⃣ 연도 선택 위젯
years = df['연도'].unique()
selected_years = st.multiselect(
    "보고 싶은 연도를 선택하세요",
    options=years,
    default=years
)

# 6️⃣ 선택된 연도만 필터링
filtered_df = df[df['연도'].isin(selected_years)]

# 7️⃣ Plotly Express 라인차트
fig = px.line(
    filtered_df,
    x='월',
    y='모기계',
    color='연도',
    markers=True,
    title="연도별·월별 모기 개체수 변화",
    labels={
        '월': '월',
        '모기계': '모기 개체수 (계)',
        '연도': '연도'
    }
)

fig.update_layout(
    xaxis=dict(tickmode='linear', dtick=1),
    yaxis=dict(title='모기 개체수 (계)'),
    hovermode='x unified'
)

# 8️⃣ Streamlit에 표시
st.plotly_chart(fig, use_container_width=True)
