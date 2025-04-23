import streamlit as st
st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()


st.title("ℹ️ Tentang Aplikasi Ini")

st.write("""
Aplikasi ini dibuat dengan **Streamlit** untuk menganalisis teks dan melakukan analisis sentimen.
Kamu bisa input teks, upload file, dan melihat hasil analisis secara langsung.
""")