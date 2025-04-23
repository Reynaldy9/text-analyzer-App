import streamlit as st
from textblob import TextBlob
st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧠 Text Analyzer")
text = st.text_area("Masukkan teks:")

if st.button("Analisa"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentimen = "Positif 😀"
    elif polarity < 0:
        sentimen = "Negatif 😠"
    else:
        sentimen = "Netral 😐"

    st.write(f"Hasil Sentimen: **{sentimen}**")
