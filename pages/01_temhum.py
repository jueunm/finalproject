import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기
df = pd.read_csv('2024_월별_기온_습도_평균.csv', header=None)

# 데이터 가공
df.columns = ['월', '평균 기온', '평균 습도']

# Streamlit 제목
st.title("월별 기온 및 습도 변화 그래프")

# 라인 차트 그리기
fig, ax1 = plt.subplots()

# 첫 번째 y축: 기온
ax1.set_xlabel('월')
ax1.set_ylabel('평균 기온 (°C)', color='tab:red')
ax1.plot(df['월'], df['평균 기온'], color='tab:red', marker='o', label='평균 기온')
ax1.tick_params(axis='y', labelcolor='tab:red')

# 두 번째 y축: 습도
ax2 = ax1.twinx()
ax2.set_ylabel('평균 습도 (%)', color='tab:blue')
ax2.plot(df['월'], df['평균 습도'], color='tab:blue', marker='s', label='평균 습도')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# 그래프 출력
st.pyplot(fig)
