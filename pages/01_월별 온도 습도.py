import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
file_path = '2024_월별_기온_습도_평균.csv'

try:
    # 파일 읽기 (인코딩 설정 중요!)
    df = pd.read_csv(file_path, header=None, encoding='cp949')
    df.columns = ['월', '평균 기온', '평균 습도']

    st.title("월별 평균 기온 및 습도 변화")

    # ----- 기온 그래프 -----
    st.subheader("🌡️ 월별 평균 기온 그래프")
    fig_temp, ax_temp = plt.subplots()
    ax_temp.plot(df['월'], df['평균 기온'], color='red', marker='o')
    ax_temp.set_xlabel("월")
    ax_temp.set_ylabel("평균 기온 (°C)")
    ax_temp.set_title("월별 평균 기온")
    st.pyplot(fig_temp)

    # ----- 습도 그래프 -----
    st.subheader("💧 월별 평균 습도 그래프")
    fig_humid, ax_humid = plt.subplots()
    ax_humid.plot(df['월'], df['평균 습도'], color='blue', marker='s')
    ax_humid.set_xlabel("월")
    ax_humid.set_ylabel("평균 습도 (%)")
    ax_humid.set_title("월별 평균 습도")
    st.pyplot(fig_humid)

except FileNotFoundError:
    st.error("CSV 파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    st.error("파일 인코딩 문제입니다. 'cp949' 또는 'utf-8-sig' 인코딩을 시도해 보세요.")
