import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ 제목
st.title("대한민국 연도별·월별 모기 개체수 변화 시각화")

# 2️⃣ 깃허브 raw URL (또는 로컬 파일)
url = "연도별_월별_모기_개체수_합계.csv"  # 깃허브 raw URL로 바꿔도 동일

# ✅ encoding='cp949' 또는 'euc-kr' 추가!
df = pd.read_csv(url, header=1, encoding='cp949')

# 3️⃣ 컬럼명 지정
df.columns = ['연도', '월', '모기계']

# 4️⃣ 데이터 타입 설정
df['연도'] = df['연도'].astype(int)
df['월'] = df['월'].astype(int)
df['모기계'] = df['모기계'].astype(int)

# 5️⃣ 연도 선택
years = df['연도'].unique()
selected_years = st.multiselect("연도를 선택하세요", years, default=years)

# 6️⃣ 선택된 연도 필터링
filtered_df = df[df['연도'].isin(selected_years)]

# 7️⃣ 라인차트 출력
fig, ax = plt.subplots(figsize=(10, 6))

for year in sorted(selected_years):
    monthly = filtered_df[filtered_df['연도'] == year]
    ax.plot(monthly['월'], monthly['모기계'], marker='o', label=str(year))

ax.set_xlabel("월")
ax.set_ylabel("모기 개체수 (계)")
ax.set_title("연도별·월별 모기 개체수 변화")
ax.legend()
ax.grid(True)

st.pyplot(fig)
