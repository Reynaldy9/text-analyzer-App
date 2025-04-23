# Harus di atas segalanya
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header global
show_header()

st.markdown("## 🧪 Pilih fitur dari sidebar untuk mulai...")


