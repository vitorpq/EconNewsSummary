# summarize.py

import sys
import json
import re # limpeza do texto
from datetime import datetime
from pathlib import Path
from langchain.docstore.document import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
import os

# Sempre procura o .env na raiz
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
CHANNEL_IDENTIFIER = os.getenv("TELEGRAM_CHANNEL")
SESSION_NAME = os.getenv("TELEGRAM_SESSION_NAME")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configuração do cache
CACHE_FILE = Path(__file__).parent / "summary_cache.json"

def load_cache():
    """Carrega o cache do arquivo JSON"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache_data):
    """Salva o cache no arquivo JSON"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=2)

def get_cache_key():
    """Gera a chave do cache baseada na data atual"""
    today = datetime.now()
    if today.weekday() == 0:  # Segunda-feira
        return f"monday_{today.strftime('%Y-%m-%d')}"
    return f"daily_{today.strftime('%Y-%m-%d')}"

# 🧠 Inicializa o LLM da Google com LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

# 🛠️ Usa a chain de resumo da LangChain
summary_prompt = PromptTemplate.from_template("""
Você é um analista financeiro e deve resumir as principais notícias do dia anterior sobre mercados, política e empresas.
Organize em tópicos, destaque os pontos mais relevantes e elimine repetições e termos promocionais.

Texto:
{input}

Resumo claro, direto e com tópicos:
""")

summarize_chain = summary_prompt | llm

def clean_text(text):
    # Remove disclaimers repetitivos
    text = re.sub(r'Disclaimer ActivTrades.*?derivativos__', '', text, flags=re.DOTALL)
    # Remove links
    text = re.sub(r'https?://\S+', '', text)
    # Remove espaçamentos excessivos
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()

def summarize(texts):
    # Verifica o cache primeiro
    cache = load_cache()
    cache_key = get_cache_key()
    
    if cache_key in cache:
        print("Usando resumo do cache...", file=sys.stderr)
        return cache[cache_key]
    
    # Se não estiver no cache, gera novo resumo
    print("Gerando novo resumo...", file=sys.stderr)
    content = "\n\n".join([clean_text(t) for t in texts])
    
    result = summarize_chain.invoke({"input": content})
    if hasattr(result, "content"):
        summary = result.content
    else:
        summary = result
    
    # Salva no cache
    cache[cache_key] = summary
    save_cache(cache)
    
    return summary

if __name__ == "__main__":
    texts = json.loads(sys.stdin.read())
    result = summarize(texts)
    print(result)


