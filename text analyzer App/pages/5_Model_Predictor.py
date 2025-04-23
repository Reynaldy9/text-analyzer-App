import streamlit as st
import joblib

st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()


st.title("🤖 Prediksi Sentimen (dengan ML)")

text = st.text_area("Masukkan teks tweet:")

if st.button("Prediksi"):
    try:
        model = joblib.load("model/sentiment_model.pkl")
        prediksi = model.predict([text])[0]
        st.success(f"Hasil Sentimen: **{prediksi}**")
    except FileNotFoundError:
        st.error("⚠️ Model belum dilatih. Silakan latih dulu di halaman 'Train Model'.")
