import streamlit as st
import pandas as pd
st.set_page_config(page_title="Text Analyzer", layout="wide")

from components.header import show_header

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil header global
show_header()


st.title("📊 Eksplorasi Dataset Sentimen")

uploaded_file = st.file_uploader("Upload dataset CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Bersihkan nama kolom dari spasi
    df.columns = df.columns.str.strip()

    st.write("🧾 Preview Dataset:")
    st.dataframe(df.head())

    st.write("🔢 Info Dataset:")
    st.text(df.info())  # gunakan st.text agar tampilannya lebih baik daripada st.write

    st.write("📈 Distribusi Sentimen:")

    if 'sentiment' in df.columns:
        st.bar_chart(df['sentiment'].value_counts())
    else:
        st.warning("⚠️ Kolom 'sentiment' tidak ditemukan di dataset. Kolom yang tersedia:")
        st.write(df.columns.tolist())
