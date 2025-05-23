# services/api_gateway/main.py
from fastapi import FastAPI
from subprocess import Popen, PIPE
import json

from dotenv import load_dotenv
from pathlib import Path
import os

# Sempre procura o .env na raiz
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
CHANNEL_IDENTIFIER = os.getenv("TELEGRAM_CHANNEL")
SESSION_NAME = os.getenv("TELEGRAM_SESSION_NAME")

app = FastAPI()

@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna o status da API.

    Returns:
        dict: Um dicionário contendo uma mensagem de status.
    """
    return {"status": "Telegram Summary API Online"}

@app.get("/resumo")
def gerar_resumo():
    """
    Endpoint que gera um resumo das mensagens do Telegram.

    Returns:
        dict: Um dicionário contendo o resumo ou uma mensagem de erro.
    """
    try:
        # Inicia o processo do coletor de mensagens do Telegram
        telegram = Popen(["python3", "services/telegram-collector/collector.py"], stdout=PIPE, stderr=PIPE)
        telegram_out, telegram_err = telegram.communicate()

        # Verifica se houve erro no coletor
        if telegram.returncode != 0:
            raise Exception(f"Erro no collector: {telegram_err.decode()}")

        # Carrega as mensagens coletadas como JSON
        mensagens = json.loads(telegram_out)

        # Inicia o processo do summarizer
        summarizer = Popen(["python3", "services/summarizer/summarize.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        summary_out, summary_err = summarizer.communicate(input=json.dumps(mensagens).encode())

        # Verifica se houve erro no summarizer
        if summarizer.returncode != 0:
            raise Exception(f"Erro no summarizer: {summary_err.decode()}")

        # Retorna o resumo
        return {"resumo": summary_out.decode()}

    except Exception as e:
        # Retorna uma mensagem de erro em caso de exceção
        return {"error": str(e)}