import streamlit as st


def show_header():
    st.markdown("""
    <div class="header">
        <div class="header-text">
            <h1>🔍 Text Analyzer App</h1>
            <p>Analisis kalimat, klasifikasi sentimen, dan pelatihan model ML langsung dari browser!</p>
        </div>
    </div>
    <hr>
    """, unsafe_allow_html=True)
