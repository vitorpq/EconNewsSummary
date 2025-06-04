# Multi-stage build para o backend FastAPI e o frontend Streamlit

# --- Etapa 1: Copiar o Código do Backend ---
# Esta etapa serve apenas para copiar os arquivos de código do backend.
FROM python:3.9-slim-buster AS backend_code
WORKDIR /app
# Copia todos os diretórios dentro de 'services' para '/app/backend/services/'
# Isso organiza seus serviços de backend sob um único diretório.
COPY services /app/backend/services/

# --- Etapa 2: Copiar o Código do Frontend ---
# Esta etapa serve apenas para copiar os arquivos de código do frontend.
FROM python:3.9-slim-buster AS frontend_code
WORKDIR /app
# Copia o conteúdo do diretório 'frontend' para '/app/frontend/'
COPY frontend /app/frontend/

# --- Etapa 3: Imagem Final de Execução ---
# Esta é a imagem que será executada. Todas as dependências devem ser instaladas aqui.
FROM python:3.9-slim-buster AS final
WORKDIR /app

# Copia o requirements.txt e instala todas as dependências.
# ISSO É CRUCIAL para que 'streamlit' e 'uvicorn' (e outras libs) estejam disponíveis.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do backend da etapa 'backend_code' para a imagem final.
# Os serviços estarão em /app/backend/services/
COPY --from=backend_code /app/backend /app/backend

# Copia o código do frontend da etapa 'frontend_code' para a imagem final.
# O frontend estará em /app/frontend/
COPY --from=frontend_code /app/frontend /app/frontend

# Define as variáveis de ambiente necessárias para a aplicação.
# Elas devem estar na imagem final para serem acessíveis em tempo de execução.
ENV TELEGRAM_API_ID=${TELEGRAM_API_ID}
ENV TELEGRAM_API_HASH=${TELEGRAM_API_HASH}
ENV TELEGRAM_CHANNEL=${TELEGRAM_CHANNEL}
ENV TELEGRAM_SESSION_NAME=${TELEGRAM_SESSION_NAME}
ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}

# Expõe as portas que as aplicações irão escutar.
EXPOSE 8000 8502

# Comando para iniciar ambas as aplicações.
# Nota: Usar '&' para rodar processos em segundo plano pode fazer o contêiner sair
# se o processo principal do shell terminar. Para uma solução mais robusta
# para gerenciar múltiplos processos, considere usar um script 'start.sh'
# ou um gerenciador de processos como 'supervisord'.
#
# IMPORTANTE: Verifique se 'backend/main:app' é o caminho correto para o seu aplicativo FastAPI.
# Se o seu 'main.py' estiver em 'services/api_gateway/main.py' dentro do contêiner,
# o caminho correto para o uvicorn seria 'backend.services.api_gateway.main:app'
# e você precisaria ajustar o PYTHONPATH.
# Exemplo: CMD PYTHONPATH=/app/backend/services uvicorn backend.services.api_gateway.main:app --host 0.0.0.0 --port 8000 & \
#          streamlit run frontend/app.py --server.address=0.0.0.0 --server.port=8502
#
# Estou mantendo seu comando original por enquanto, assumindo que seu código
# interno lida com o caminho 'backend/main:app' corretamente.
CMD PYTHONPATH=/app uvicorn backend.services.api_gateway.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/app.py --server.address=0.0.0.0 --server.port=8502