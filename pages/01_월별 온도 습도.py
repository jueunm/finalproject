import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
file_path = '2024_월별_기온_습도_평균.csv'

try:
    df = pd.read_csv(file_path, header=None, encoding='cp949')
    df.columns = ['월', '평균 기온', '평균 습도']

    # '월' 열을 정수로 안전하게 변환
    df['월'] = pd.to_numeric(df['월'], errors='coerce')
    df = df.dropna(subset=['월'])
    df['월'] = df['월'].astype(int)
    df = df.sort_values('월')

    st.title("월별 평균 기온 및 습도 변화")

    # 🌡️ 기온 그래프
    st.subheader("🌡️ 월별 평균 기온 그래프")
    fig_temp, ax_temp = plt.subplots()
    ax_temp.plot(df['월'], df['평균 기온'], color='red', marker='o')
    ax_temp.set_xlabel("월")
    ax_temp.set_ylabel("평균 기온 (°C)")
    ax_temp.set_title("월별 평균 기온")
    ax_temp.set_xticks(df['월'])
    st.pyplot(fig_temp)

    # 💧 습도 그래프
    st.subheader("💧 월별 평균 습도 그래프")
    fig_humid, ax_humid = plt.subplots()
    ax_humid.plot(df['월'], df['평균 습도'], color='blue', marker='s')
    ax_humid.set_xlabel("월")
    ax_humid.set_ylabel("평균 습도 (%)")
    ax_humid.set_title("월별 평균 습도")
    ax_humid.set_xticks(df['월'])
    st.pyplot(fig_humid)

except FileNotFoundError:
    st.error("CSV 파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    st.error("파일 인코딩 문제입니다. 'cp949' 또는 'utf-8-sig' 인코딩을 시도해 보세요.")
except ValueError as e:
    st.error(f"값 변환 중 오류 발생: {e}")
