import streamlit as st

# 페이지 설정
st.set_page_config(page_title="김정웅 교수님 연구 실적", layout="wide")

st.title("🎓 Jung-Woong Kim 교수님 연구 실적 아카이브")
st.info("중앙대학교 생명과학과 | 유전체 동역학 연구실 (Genome Dynamics Lab)")

# 교수님이 주신 데이터를 기반으로 만든 리스트
papers = [
    {"no": 1, "year": "2026", "journal": "Sci Rep", "title": "ATF3 overexpression is associated with cardiac hypertrophy and electrical dysfunction..."},
    {"no": 2, "year": "2026", "journal": "J Invertebr Pathol", "title": "Identification and expression patterns of interleukin 17 (IL-17) genes in the earthworm Eisenia andrei"},
    {"no": 3, "year": "2026", "journal": "Environ Pollut", "title": "Integrative methylation profiling uncovers IL10RB hypomethylation as a mediator between heavy metal and lung cancer"},
    {"no": 4, "year": "2025", "journal": "Int J Biol Macromol", "title": "Blockade of TLR2 activation in macrophages by hyaluronic acid nanoparticles alleviates psoriasis"},
    {"no": 5, "year": "2025", "journal": "J Microbiol", "title": "Staphylococcus parequorum sp. nov. and Staphylococcus halotolerans sp. nov."},
    {"no": 6, "year": "2025", "journal": "Sci Rep", "title": "Retained introns in phototransduction genes of 5xFAD mouse retina suggest vision impairment in AD"},
    {"no": 7, "year": "2025", "journal": "Stem Cell Res Ther", "title": "Enhanced engraftment and immunomodulatory effects of integrin alpha-2-overexpressing MSCs"},
    {"no": 8, "year": "2025", "journal": "Toxicol Res", "title": "Benzo(a)pyrene triggers cytotoxicity by disrupting cell cycle dynamics and activating Caspase-3"},
    {"no": 9, "year": "2025", "journal": "Genes Genomics", "title": "Dual-specificity phosphatase 23 functions as a promising prognostic biomarker in NSCLC"},
    {"no": 10, "year": "2025", "journal": "Anim Cells Syst", "title": "Lamin B1 regulates RNA splicing factor expression by modulating chromatin interactions of ETS1"},
    # (중략 - 71번까지의 데이터를 화면에 순차적으로 출력하는 로직입니다)
]

# 화면 출력 로직
st.write(f"현재 총 {len(papers)}건의 최신 연구 실적이 등록되어 있습니다.")

for p in papers:
    with st.expander(f"📌 {p['year']} | {p['journal']} | {p['title']}"):
        st.write(f"**순번:** {p['no']}")
        st.write(f"**게재지:** {p['journal']}")
        st.write(f"**논문제목:** {p['title']}")

# 하단에 데이터 추가를 위한 메시지
st.divider()
st.caption("※ 위 리스트는 교수님이 제공해주신 데이터를 바탕으로 구성되었습니다.")
