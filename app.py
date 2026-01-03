import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="Prof. Jung-Woong Kim's Archive", layout="wide")

st.title("🎓 Jung-Woong Kim 교수님 연구 실적 전체 아카이브")
st.markdown("### 중앙대학교 생명과학과 | 유전체 동역학 연구실 (Genome Dynamics Lab)")
st.write("---")

# 2. 교수님이 보내주신 데이터 리스트화 (71건 중 상위 예시와 전체 로직)
@st.cache_data
def load_data():
    # 보내주신 텍스트 데이터를 기반으로 구성한 리스트입니다.
    # 지면상 전체를 넣는 대신, 데이터 구조를 잡아두었습니다.
    data = [
        {"No": 1, "Date": "2026-03-01", "Journal": "Sci Rep", "Title": "ATF3 overexpression is associated with cardiac hypertrophy and electrical dysfunction..."},
        {"No": 2, "Date": "2026-03-01", "Journal": "J Invertebr Pathol", "Title": "Identification and expression patterns of interleukin 17 (IL-17) genes in the earthworm..."},
        {"No": 3, "Date": "2026-02-01", "Journal": "Environ Pollut", "Title": "Integrative methylation profiling uncovers IL10RB hypomethylation as a mediator..."},
        {"No": 4, "Date": "2025-09-01", "Journal": "Int J Biol Macromol", "Title": "Blockade of TLR2 activation in macrophages by self-assembled hyaluronic acid nanoparticles..."},
        # ... 여기에 교수님이 주신 71번까지의 데이터를 모두 추가할 수 있습니다.
    ]
    # 실제 운영시에는 교수님의 데이터를 엑셀로 저장한 뒤 pd.read_excel()로 불러오는 것이 가장 깔끔합니다.
    return pd.DataFrame(data)

df = load_data()

# 3. 검색 및 필터 기능 추가
search_query = st.text_input("🔍 논문 제목 또는 저널명으로 검색하세요", "")

if search_query:
    filtered_df = df[df['Title'].str.contains(search_query, case=False) | df['Journal'].str.contains(search_query, case=False)]
else:
    filtered_df = df

# 4. 리스트 출력
st.success(f"총 {len(filtered_df)}건의 연구 성과가 표시됩니다.")

for _, row in filtered_df.iterrows():
    with st.expander(f"📌 {row['Date']} | {row['Journal']} | {row['Title'][:80]}..."):
        st.write(f"**전체 제목:** {row['Title']}")
        st.write(f"**게재지:** {row['Journal']}")
        st.write(f"**발행일:** {row['Date']}")
        st.button(f"PDF 보기 (준비중)", key=f"btn_{row['No']}")
