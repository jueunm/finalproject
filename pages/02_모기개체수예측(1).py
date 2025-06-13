import streamlit as st
import pandas as pd
import glob

# 페이지 설정
st.set_page_config(page_title="🦟 예측 vs 실제 비교 (2024)", layout="centered")
st.title("🔮 예측 vs 실제 – 2024년 월별 모기 개체수 비교")

# — 1. 과거 데이터 로드 & 예측 계산 —
url = "연도별_월별_모기_개체수_합계.csv"
df = pd.read_csv(url, header=1, encoding='cp949')
df.columns = ['연도','월','모기계']
df[['연도','월','모기계']] = df[['연도','월','모기계']].astype(int)

N = st.slider("예측에 사용할 최근 N년", 1, 10, 5)
recent_start = df['연도'].max() - N + 1
recent_df = df[df['연도']>=recent_start]
pred = recent_df.groupby('월')['모기계'].mean().round().astype(int).reset_index()
pred['연도'] = 2024

# — 2. 실제 2024 데이터 불러오기 —
xlsx_files = glob.glob("2024*_유문등.xlsx")
real_list = []
for f in xlsx_files:
    m = int(f.split("2024년 ")[1][:2])  # 파일명에서 월 추출
    tmp = pd.read_excel(f, skiprows=1)  # 헤더 행 위치는 파일마다 다를 수 있어 조정 필요
    total = tmp['개체수'].sum()
    real_list.append({'연도':2024, '월':m, '모기계':int(total)})
real = pd.DataFrame(real_list)

# 병합 & 비교
comp = pd.merge(pred, real, on=['연도','월'], how='outer', suffixes=('_예측','_실제')).sort_values('월')

# 📊 표 출력
st.subheader(f"📋 예측 vs 실제 (최근 {N}년 평균 기반)")
st.dataframe(comp)

# — 3. 수학적 설명 —
st.markdown(f"""
### 🧮 예측 공식 (월별 평균)
$$
E_{{2024,m}} = \\frac{1}{N} \\sum_{{y={recent_start}}}^{{2023}} X_{{y,m}}
$$
- $E_{{2024,m}}$: 2024년 m월 예측값  
- $N$: 최근 {N}년 ( {recent_start}–2023 )  
- $X_{{y,m}}$: y년도 m월 실제 모기 개체수  

### 📌 실제 데이터
- 서울 열린데이터광장의 2024년도 유문등 채집 자료 (4~11월) :contentReference[oaicite:5]{index=5}

""")

st.success("✅ 예측값과 실제값을 비교해보세요!")
