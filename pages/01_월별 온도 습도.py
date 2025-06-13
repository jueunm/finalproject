import streamlit as st
import pandas as pd
import plotly.express as px

# 파일 경로
file_path = '2024_월별_기온_습도_평균.csv'

try:
    # 파일 읽기
    df = pd.read_csv(file_path, header=None, encoding='cp949')
    df.columns = ['월', '평균 기온', '평균 습도']

    # '월' 정리
    df['월'] = pd.to_numeric(df['월'], errors='coerce')
    df = df.dropna(subset=['월'])
    df['월'] = df['월'].astype(int)
    df = df.sort_values('월')

    st.title("📊 월별 평균 기온 및 습도 변화 (Plotly 그래프)")

    # 🌡️ 평균 기온 그래프
    st.subheader("🌡️ 월별 평균 기온")
    fig_temp = px.line(
        df, x='월', y='평균 기온',
        markers=True,
        title="월별 평균 기온 (°C)",
        labels={'월': '월', '평균 기온': '기온 (°C)'},
        line_shape='spline'
    )
    fig_temp.update_traces(line=dict(color='red'))
    st.plotly_chart(fig_temp, use_container_width=True)

    # 💧 평균 습도 그래프
    st.subheader("💧 월별 평균 습도")
    fig_humid = px.line(
        df, x='월', y='평균 습도',
        markers=True,
        title="월별 평균 습도 (%)",
        labels={'월': '월', '평균 습도': '습도 (%)'},
        line_shape='spline'
    )
    fig_humid.update_traces(line=dict(color='blue'))
    st.plotly_chart(fig_humid, use_container_width=True)

except FileNotFoundError:
    st.error("CSV 파일을 찾을 수 없습니다.")
except UnicodeDecodeError:
    st.error("파일 인코딩 문제입니다. 'cp949' 또는 'utf-8-sig' 인코딩을 시도해 보세요.")
except Exception as e:
    st.error(f"오류 발생: {e}")
