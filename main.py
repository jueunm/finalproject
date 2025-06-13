import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ 제목
st.title("대한민국 연도별·월별 모기 개체수 변화 시각화")

# 3️⃣ CSV 파일 읽기 (2행부터 데이터라고 하셨으니, header=1로 설정)
df = pd.read_csv('연도별_월별_모기_개체수_합계.csv',header=1)

# 4️⃣ 컬럼명 확인 & 필요하다면 설정
# 예: ['연도', '월', '모기계']
df.columns = ['연도', '월', '모기계']

# 5️⃣ 데이터 타입 확인 & 필요시 변환
df['연도'] = df['연도'].astype(int)
df['월'] = df['월'].astype(int)
df['모기계'] = df['모기계'].astype(int)

# 6️⃣ 연도 선택 옵션
years = df['연도'].unique()
selected_years = st.multiselect("연도를 선택하세요", years, default=years)

# 7️⃣ 선택된 연도 필터링
filtered_df = df[df['연도'].isin(selected_years)]

# 8️⃣ 라인 차트 그리기
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
