import streamlit as st
from textblob import TextBlob
import joblib

st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()

st.title("🔍 Perbandingan TextBlob vs ML Sentiment")

text = st.text_area("Masukkan teks:")

if st.button("Bandingkan") and text:
    # TextBlob prediction
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        tb_sentiment = "Positive"
    elif polarity < 0:
        tb_sentiment = "Negative"
    else:
        tb_sentiment = "Neutral"

    # ML prediction
    try:
        model = joblib.load("model/sentiment_model.pkl")
        ml_sentiment = model.predict([text])[0]
    except FileNotFoundError:
        ml_sentiment = "Model belum dilatih."

    # Display comparison
    st.markdown("### 📊 Hasil Perbandingan:")
    col1, col2 = st.columns(2)
    col1.metric("TextBlob", tb_sentiment)
    col2.metric("ML Model", ml_sentiment)
