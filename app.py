import streamlit as st
from Bio import Entrez
import pandas as pd

# 1. 설정 및 기본 정보
Entrez.email = "your_email@example.com"
# 교수님 성함과 소속을 더 정확하게 매칭하는 쿼리
QUERY = '(Kim JW[Author]) AND (Chung-Ang University[Affiliation])'

st.set_page_config(page_title="Prof. Jung-Woong Kim's Lab", layout="wide")
st.title("🎓 Jung-Woong Kim 교수님 논문 아카이브")
st.markdown("##### 중앙대학교 (2015 - 현재 발표 논문)")

# 2. 데이터 가져오기 함수 (더 정밀하게 수정)
def get_papers():
    # 2015년부터 검색
    handle = Entrez.esearch(db="pubmed", term=QUERY, mindate="2015/01/01", retmax=100)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    if not ids: return []

    fetch_handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
    lines = fetch_handle.readlines()
    fetch_handle.close()

    papers, current = [], {}
    for line in lines:
        if line.startswith("TI  - "): current["Title"] = line[6:].strip()
        elif line.startswith("DP  - "): current["Date"] = line[6:].strip()
        elif line.startswith("TA  - "): current["Journal"] = line[6:].strip()
        elif line.startswith("AID - ") and "[doi]" in line: 
            current["DOI"] = line[6:].replace("[doi]", "").strip()
        elif line.startswith("AB  - "): current["Abstract"] = line[6:].strip()
        elif line.strip() == "" and current:
            papers.append(current)
            current = {}
    return papers

# 3. 화면 UI 구성
if st.button('🔄 최신 논문 실시간 업데이트'):
    with st.spinner('PubMed 서버에서 논문을 분석 중입니다...'):
        results = get_papers()
        st.session_state['results'] = results

if 'results' in st.session_state:
    data = st.session_state['results']
    st.success(f"총 {len(data)}개의 연구 성과를 찾았습니다.")
    
    # 데이터를 표 형식으로 정리
    df = pd.DataFrame(data)
    
    # 논문 하나씩 카드 형태로 출력
    for idx, row in df.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 8])
            col1.metric("Year", row['Date'][:4])
            with col2:
                st.subheader(row['Title'])
                st.caption(f"📓 Journal: {row.get('Journal', 'N/A')}")
                
                with st.expander("초록(Abstract) 보기"):
                    st.write(row.get('Abstract', '초록 내용이 없습니다.'))
                
                if 'DOI' in row:
                    st.link_button("📄 원문 링크(DOI) 이동", f"https://doi.org/{row['DOI']}")
            st.divider()
