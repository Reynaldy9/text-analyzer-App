import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()


st.title("🧠 Train Model Sentimen")

uploaded_file = st.file_uploader("Upload dataset CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset dimuat!")

    st.write("🔢 Contoh data:")
    st.write(df.head())

    if st.button("Latih Model"):

        X = df['tweet']  # Ganti jika kolomnya bukan 'Tweet'
        y = df['sentiment']

        model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', MultinomialNB())
        ])
        model.fit(X, y)

        if not os.path.exists("model"):
            os.mkdir("model")

        joblib.dump(model, "model/sentiment_model.pkl")
        df.to_csv("model/sentiment_model.csv", index=False)
        st.success("✅ Model berhasil dilatih dan disimpan!")
