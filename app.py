import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Virtual Lab AAS Cu", page_icon="🔬", layout="wide")

# Hilangkan jarak dan header bawaan Streamlit supaya lab tampil penuh
st.markdown(
    """
    <style>
    .block-container{padding:0 !important;max-width:100% !important}
    header[data-testid="stHeader"]{display:none}
    footer{visibility:hidden}
    </style>
    """,
    unsafe_allow_html=True,
)

html_file = Path(__file__).parent / "index.html"
if html_file.exists():
    components.html(html_file.read_text(encoding="utf-8"), height=900, scrolling=False)
else:
    st.error("File index.html tidak ditemukan. Letakkan di folder yang sama dengan app.py.")
