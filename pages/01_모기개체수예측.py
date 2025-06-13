import streamlit as st
import pandas as pd

# ------------------------
# 🎯 페이지 설정
# ------------------------

st.set_page_config(
    page_title="🔮 2024년 모기 개체수 예측",
    page_icon="🦟",
    layout="centered"
)

st.title("🔮🦟 2024년 월별 모기 개체수 예측")
st.markdown(
    """
    ## 📅 예측 개요  
    아래 표는 **최근 N년간 월별 평균값**을 기반으로 **2024년 모기 개체수**를 예측한 결과입니다.  
    복잡한 시계열 모델 대신, 계절성 패턴을 그대로 반영하는 단순 평균 방식을 사용했습니다.
    """
)

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
# 🔢 최근 몇 년 평균으로 할지 선택
# ------------------------

N = st.slider("최근 몇 년간의 데이터를 사용할까요?", min_value=1, max_value=10, value=5)

recent_start = df['연도'].max() - N + 1
recent_df = df[df['연도'] >= recent_start]

# ------------------------
# ✅ 예측값 계산 (단순 월별 평균)
# ------------------------

monthly_forecast = recent_df.groupby('월')['모기계'].mean().reset_index()
monthly_forecast['모기계'] = monthly_forecast['모기계'].round().astype(int)
monthly_forecast['연도'] = 2024
monthly_forecast = monthly_forecast[['연도', '월', '모기계']]

# ------------------------
# 📋 예측표 출력
# ------------------------

st.subheader(f"📊 2024년 월별 모기 개체수 예측 (최근 {N}년 평균 기반)")
st.dataframe(monthly_forecast)

# ------------------------
# 📐 수학적 원리 설명
# ------------------------

st.markdown(
    f"""
    ## 🧮 수학적 계산 방식
    
    2024년 `{N}`년 평균 예측 값은 아래 공식으로 계산됩니다:
    
    \n
    \\[
    E_{{2024, m}} = \\frac{{1}}{{{N}}} \\sum_{{y={recent_start}}}^{{2023}} X_{{y, m}}
    \\]
    
    - \\( E_{{2024, m}} \\): 2024년 m월 모기 개체수 예측값  
    - \\( X_{{y, m}} \\): 연도 y의 m월 모기 개체수  
    - 최근 {N}년( {recent_start} ~ 2023 )의 같은 달 평균을 사용합니다.
    
    ---
    
    📌 **왜 이렇게 하나요?**  
    - 모기 개체수는 기온과 강수량의 계절적 영향으로 월별 패턴이 강합니다.  
    - 복잡한 예측보다 과거의 계절 평균이 실제 발생량과 가장 유사할 수 있습니다.  
    - 기후 변화 등 장기적 추세가 없다면 신뢰도가 높습니다.
    """
)

st.success("✨ 예측 결과를 바탕으로 모기 방역 계획을 세워보세요!")
