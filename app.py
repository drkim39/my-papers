import streamlit as st
from Bio import Entrez
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(page_title="Prof. Kim's Archive", layout="wide")
Entrez.email = "example@cau.ac.kr" # 아무 이메일이나 넣어도 작동합니다.

# 2. 제목 부분
st.title("🎓 Jung-Woong Kim 교수님 연구 아카이브")
st.markdown("---")

# 3. 데이터 수집 및 정제 함수
def fetch_and_clean_data():
    query = '(Kim JW[Author]) AND (Chung-Ang University[Affiliation])'
    handle = Entrez.esearch(db="pubmed", term=query, mindate="2015/01/01", retmax=50)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    if not ids: return []

    fetch_handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
    raw_data = fetch_handle.read()
    fetch_handle.close()

    papers = []
    # 원시 데이터를 논문 단위로 자르기
    raw_papers = raw_data.split("\n\n")
    
    for rp in raw_papers:
        if not rp.strip(): continue
        paper_info = {}
        for line in rp.split("\n"):
            if line.startswith("TI  - "): paper_info["Title"] = line[6:].strip()
            elif line.startswith("DP  - "): paper_info["Date"] = line[6:].strip()
            elif line.startswith("TA  - "): paper_info["Journal"] = line[6:].strip()
            elif line.startswith("AB  - "): paper_info["Abstract"] = line[6:].strip()
            elif line.startswith("LID - ") and "doi" in line:
                paper_info["DOI"] = line[6:].split(" [")[0].strip()
        
        if paper_info: papers.append(paper_info)
    
    return papers

# 4. 앱 화면 구현
if st.button('🔄 최신 논문 실시간 업데이트'):
    with st.spinner('데이터를 정제 중입니다...'):
        st.session_state['cleaned_data'] = fetch_and_clean_data()

if 'cleaned_data' in st.session_state:
    data = st.session_state['cleaned_data']
    st.write(f"✅ 총 **{len(data)}**개의 연구 성과를 찾았습니다.")
    
    for p in data:
        # 논문 한 장씩 깔끔한 박스에 담기
        with st.expander(f"📅 {p.get('Date', 'N/A')} | {p.get('Title', 'No Title')}"):
            st.markdown(f"**저널명:** {p.get('Journal', 'N/A')}")
            if 'DOI' in p:
                st.markdown(f"**DOI:** [https://doi.org/{p['DOI']}](https://doi.org/{p['DOI']})")
            st.markdown(f"**초록(Abstract):**")
            st.write(p.get('Abstract', '내용 없음'))
