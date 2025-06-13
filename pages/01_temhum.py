import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
file_path = '2024_월별_기온_습도_평균.csv'

# CSV 읽기 (인코딩 주의!)
try:
    df = pd.read_csv(file_path, header=None, encoding='cp949')
    df.columns = ['월', '평균 기온', '평균 습도']

    # 제목
    st.title("월별 기온 및 습도 변화")

    # 그래프
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('월')
    ax1.set_ylabel('평균 기온 (°C)', color='red')
    ax1.plot(df['월'], df['평균 기온'], color='red', marker='o')
    ax1.tick_params(axis='y', labelcolor='red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('평균 습도 (%)', color='blue')
    ax2.plot(df['월'], df['평균 습도'], color='blue', marker='s')
    ax2.tick_params(axis='y', labelcolor='blue')

    st.pyplot(fig)

except FileNotFoundError:
    st.error("CSV 파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    st.error("CSV 파일 인코딩을 확인하세요. 'cp949' 또는 'utf-8-sig'로 시도해보세요.")
