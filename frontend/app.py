# frontend/app.py

import streamlit as st
import requests

API_URL = "http://localhost:8080/resumo"  # ou a URL do seu deploy Railway

def format_markdown(summary):
    return "\n".join([
        f"### 📌 {line.strip()}" if line.startswith("*") or line.startswith("▶️") else line
        for line in summary.split("\n") if line.strip()
    ])

st.set_page_config(page_title="Resumo de Notícias - Telegram", layout="wide")

st.title("📰 Resumo Diário de Notícias")
st.markdown("Este resumo foi gerado automaticamente com Gemini + LangChain.")

if st.button("🔄 Atualizar resumo"):
    with st.spinner("Gerando resumo..."):
        try:
            response = requests.get(API_URL, timeout=30)
            data = response.json()
            resumo = data.get("resumo", "")
            st.success("Resumo atualizado com sucesso!")
            st.markdown(format_markdown(resumo))
            
        except Exception as e:
            st.error(f"Erro ao buscar resumo: {e}")
else:
    st.info("Clique no botão acima para carregar o resumo.")