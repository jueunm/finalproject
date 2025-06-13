import streamlit as st
import pandas as pd

st.set_page_config(page_title="🦟 2024년 모기 예측 vs 실제 비교", layout="centered")
st.title("🔮 2024년 모기 개체수 예측 vs 실제 비교")

df = pd.read_csv("연도별_월별_모기_개체수_합계.csv", header=1, encoding='cp949')
df.columns = ['연도', '월', '모기계']
df[['연도', '월', '모기계']] = df[['연도', '월', '모기계']].astype(int)

N = st.slider("최근 몇 년 데이터로 평균 예측할까요?", 1, 10, 5)
recent_start = df['연도'].max() - N + 1
recent_df = df[df['연도'] >= recent_start]

pred = recent_df.groupby('월')['모기계'].mean().round().astype(int).reset_index()
pred['연도'] = 2024

real_dict = {
    4: 214, 5: 858, 6: 2034, 7: 2511, 8: 2146,
    9: 2285, 10: 5087, 11: 1862
}
real = pd.DataFrame({
    '연도': 2024,
    '월': list(real_dict.keys()),
    '모기계': list(real_dict.values())
})

comp = pd.merge(pred, real, on=['연도', '월'], how='outer', suffixes=('_예측', '_실제')).sort_values('월')

comp['오차(실제-예측)'] = comp['모기계_실제'] - comp['모기계_예측']
comp['오차율(%)'] = (comp['오차(실제-예측)'].abs() / comp['모기계_실제'] * 100).round(2)

st.subheader(f"📊 2024년 모기 개체수 예측 vs 실제 비교 (최근 {N}년 평균 기준)")
st.dataframe(comp.style.format({
    '모기계_예측': '{:,}', '모기계_실제': '{:,}',
    '오차(실제-예측)': '{:,}', '오차율(%)': '{:.2f}%'
}))

st.markdown(f"""
### 🧮 예측 수식

2024년 각 월의 모기 개체수 예측값은 최근 {N}년 동안 해당 월의 평균 모기 개체수로 계산했습니다:

$$
E_{{2024,m}} = \\frac{{1}}{{{N}}} \\sum_{{y={recent_start}}}^{{2023}} X_{{y,m}}
$$

- $E_{{2024,m}}$: 2024년 m월의 예측 모기 개체수  
- $N$: 최근 {N}년  
- $X_{{y,m}}$: y년도 m월의 실제 모기 개체수  

### ✅ 실제 데이터  
2024년 4월부터 11월까지 서울 열린데이터광장에서 제공된 유문등 채집 모기 개체수를 바탕으로 직접 입력했습니다.
""")
