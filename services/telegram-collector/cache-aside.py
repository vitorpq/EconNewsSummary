import time
import hashlib

# --- Simulação de Cache em Memória ---
# Em um cenário real, você usaria Redis, Memcached ou uma biblioteca como cachetools.
# Para este exemplo, um dicionário Python servirá.
cache_storage = {}
DEFAULT_TTL = 300  # Tempo de vida padrão para entradas de cache em segundos (5 minutos)

# --- Simulação de Clientes de API ---

def fetch_news_from_telegram_api(channel_id: str, message_id: str) -> dict:
    """
    Simula uma chamada à API do Telegram para buscar uma notícia.
    Introduz um atraso para simular a latência da rede/API.
    """
    print(f" Buscando notícia: canal='{channel_id}', mensagem='{message_id}'...")
    time.sleep(2)  # Simula a latência da API
    # Conteúdo simulado da notícia
    news_content = {
        "id": message_id,
        "channel": channel_id,
        "text": f"Esta é uma notícia muito importante do canal {channel_id} com ID {message_id}. " * 5,
        "timestamp": time.time()
    }
    print(f" Notícia '{channel_id}/{message_id}' recebida.")
    return news_content

def summarize_with_gemini_api(article_text: str, summary_length: str = "curto") -> str:
    """
    Simula uma chamada à API Gemini para sumarizar um texto.
    Introduz um atraso para simular o processamento da IA.
    """
    print(f"[API Gemini] Sumarizando texto (comprimento: {summary_length})...")
    time.sleep(3)  # Simula a latência e processamento da IA
    summary = f"Sumário ({summary_length}): {article_text[:50]}..."
    print(f"[API Gemini] Sumário gerado.")
    return summary

# --- Funções de Cache ---

def _generate_cache_key(*args) -> str:
    """
    Gera uma chave de cache consistente a partir dos argumentos fornecidos.
    Usa hash para garantir que a chave seja uma string de tamanho gerenciável e
    para lidar com argumentos complexos, se necessário.
    """
    key_parts = [str(arg) for arg in args]
    key_string = ":".join(key_parts)
    return hashlib.md5(key_string.encode('utf-8')).hexdigest()

def get_from_cache(key: str):
    """
    Obtém um item do cache se existir e não estiver expirado.
    """
    if key in cache_storage:
        item = cache_storage[key]
        # Verifica o TTL
        if time.time() < item['expires_at']:
            print(f"[Cache] Cache HIT para a chave '{key}'.")
            return item['value']
        else:
            print(f"[Cache] Cache STALE (expirado) para a chave '{key}'. Removendo.")
            del cache_storage[key] # Remove item expirado
    print(f"[Cache] Cache MISS para a chave '{key}'.")
    return None

def set_in_cache(key: str, value, ttl_seconds: int = DEFAULT_TTL):
    """
    Adiciona um item ao cache com um tempo de vida (TTL).
    """
    expires_at = time.time() + ttl_seconds
    cache_storage[key] = {
        'value': value,
        'expires_at': expires_at
    }
    print(f"[Cache] Item adicionado/atualizado no cache para a chave '{key}' com TTL de {ttl_seconds}s.")

# --- Lógica da Aplicação com Cache-Aside ---

def get_telegram_news_with_cache(channel_id: str, message_id: str) -> dict:
    """
    Obtém uma notícia do Telegram, utilizando o padrão cache-aside.
    """
    cache_key = _generate_cache_key("telegram_news", channel_id, message_id)

    # 1. Tenta obter do cache
    cached_news = get_from_cache(cache_key)
    if cached_news:
        return cached_news

    # 2. Cache miss: busca da fonte original (API do Telegram)
    news_data = fetch_news_from_telegram_api(channel_id, message_id)

    # 3. Armazena no cache
    if news_data: # Só cacheia se a API retornou algo
        set_in_cache(cache_key, news_data, ttl_seconds=3600) # TTL de 1 hora para notícias

    return news_data

def get_gemini_summary_with_cache(article_text: str, summary_length: str = "curto") -> str:
    """
    Obtém um sumário do Gemini, utilizando o padrão cache-aside.
    A chave de cache inclui o texto do artigo e o comprimento do sumário.
    """
    # É importante que a chave de cache para o sumário dependa do conteúdo do artigo
    # e de quaisquer parâmetros que afetem a saída do sumário.
    cache_key = _generate_cache_key("gemini_summary", article_text, summary_length)

    # 1. Tenta obter do cache
    cached_summary = get_from_cache(cache_key)
    if cached_summary:
        return cached_summary

    # 2. Cache miss: busca da fonte original (API Gemini)
    summary_data = summarize_with_gemini_api(article_text, summary_length)

    # 3. Armazena no cache
    if summary_data: # Só cacheia se a API retornou algo
        set_in_cache(cache_key, summary_data, ttl_seconds=1800) # TTL de 30 minutos para sumários

    return summary_data

# --- Demonstração de Uso ---
if __name__ == "__main__":
    print("--- Iniciando Demonstração do Cache-Aside ---")

    # Cenário 1: Buscar uma notícia e seu sumário pela primeira vez (Cache Miss)
    print("\n=== Tentativa 1: Notícia 'canal_A/msg_001' ===")
    noticia_1 = get_telegram_news_with_cache("canal_A", "msg_001")
    if noticia_1:
        sumario_1 = get_gemini_summary_with_cache(noticia_1["text"], summary_length="médio")
        print(f"\nNotícia Original: {noticia_1['text'][:100]}...")
        print(f"Sumário Gerado: {sumario_1}")

    print("\n" + "="*50 + "\n")

    # Cenário 2: Buscar a mesma notícia e sumário novamente (Cache Hit)
    print("\n=== Tentativa 2: Notícia 'canal_A/msg_001' (deve vir do cache) ===")
    noticia_1_cached = get_telegram_news_with_cache("canal_A", "msg_001")
    if noticia_1_cached:
        sumario_1_cached = get_gemini_summary_with_cache(noticia_1_cached["text"], summary_length="médio")
        print(f"\nNotícia do Cache: {noticia_1_cached['text'][:100]}...")
        print(f"Sumário do Cache: {sumario_1_cached}")

    print("\n" + "="*50 + "\n")

    # Cenário 3: Buscar uma notícia diferente (Cache Miss)
    print("\n=== Tentativa 3: Notícia 'canal_B/msg_002' ===")
    noticia_2 = get_telegram_news_with_cache("canal_B", "msg_002")
    if noticia_2:
        sumario_2 = get_gemini_summary_with_cache(noticia_2["text"], summary_length="curto")
        print(f"\nNotícia Original: {noticia_2['text'][:100]}...")
        print(f"Sumário Gerado: {sumario_2}")

    print("\n" + "="*50 + "\n")

    # Cenário 4: Esperar o TTL da notícia 1 expirar (usando um TTL curto para demonstração)
    print("\n=== Demonstração de Expiração de Cache (TTL) ===")
    # Vamos buscar a notícia 1 novamente, mas antes, vamos alterar seu TTL para algo curto
    # e simular a passagem do tempo.
    # (Em um código real, você não alteraria o TTL assim, mas para fins de demo:)
    if _generate_cache_key("telegram_news", "canal_A", "msg_001") in cache_storage:
        print("Alterando TTL da notícia 'canal_A/msg_001' para 5 segundos para demonstração...")
        set_in_cache(_generate_cache_key("telegram_news", "canal_A", "msg_001"),
                     cache_storage[_generate_cache_key("telegram_news", "canal_A", "msg_001")]['value'],
                     ttl_seconds=5)

    print("Esperando 7 segundos para o cache da notícia 'canal_A/msg_001' expirar...")
    time.sleep(7)

    print("\n=== Tentativa 4: Notícia 'canal_A/msg_001' (após TTL expirar - deve ser Cache Miss) ===")
    noticia_1_apos_ttl = get_telegram_news_with_cache("canal_A", "msg_001")
    if noticia_1_apos_ttl:
        print(f"\nNotícia (após expiração): {noticia_1_apos_ttl['text'][:100]}...")
        # O sumário ainda pode estar no cache se seu TTL for maior e a chave (baseada no texto) não mudou
        sumario_1_apos_ttl = get_gemini_summary_with_cache(noticia_1_apos_ttl["text"], summary_length="médio")
        print(f"Sumário (após expiração da notícia): {sumario_1_apos_ttl}")


    print("\n--- Fim da Demonstração ---")
    print(f"\nEstado final do cache_storage: {len(cache_storage)} itens")
    # for k, v in cache_storage.items():
    #     print(f"  Chave: {k}, Expira em: {time.strftime('%H:%M:%S', time.localtime(v['expires_at']))}")