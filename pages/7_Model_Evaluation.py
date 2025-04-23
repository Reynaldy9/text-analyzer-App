import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import classification_report

st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()


st.title("📈 Evaluasi Model ML")

file = st.file_uploader("Upload dataset untuk evaluasi", type="csv")

if file:
    df = pd.read_csv(file)

    try:
        model = joblib.load("model/sentiment_model.pkl")
        X_test = df['tweet']
        y_test = df['sentiment']
        y_pred = model.predict(X_test)

        report = classification_report(y_test, y_pred, output_dict=False)
        st.text("Classification Report:")
        st.code(report)

    except FileNotFoundError:
        st.error("Model belum dilatih.")
