import streamlit as st
from Bio import Entrez
import pandas as pd

st.set_page_config(page_title="Kim's Archive", layout="wide")
Entrez.email = "test@email.com"

st.title("🎓 Jung-Woong Kim 교수님 논문 아카이브")

query = "(Kim JW[Author]) AND (Chung-Ang University[Affiliation])"

if st.button('🔄 최신 논문 불러오기'):
    handle = Entrez.esearch(db="pubmed", term=query, mindate="2015/01/01")
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    if ids:
        fetch_handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
        st.success(f"{len(ids)}개의 논문을 찾았습니다.")
        st.text(fetch_handle.read()[:2000] + "...") # 우선 텍스트로 출력 확인
    else:
        st.warning("논문을 찾지 못했습니다.")
