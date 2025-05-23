FROM python:3.11-slim

WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do serviço
COPY . .

# Define as variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Comando para executar o serviço
CMD ["python", "collector.py"] 