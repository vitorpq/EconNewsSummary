import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import datetime
import os

# --- Configurações ---
API_ID = 6942037  # Substitua pelo seu API ID (inteiro)
API_HASH = 'c773a928384aa55437efad4823467f32'  # Substitua pelo seu API Hash (string)
PHONE_NUMBER = '+5571987946284'  # Ex: +55119XXXXXXXX

# Identificador do canal (ex: '@nomecanalpublico' ou o ID numérico -100xxxxxxxxxx)
CHANNEL_IDENTIFIER = '@activtradespt'

# Arquivo para guardar o ID da última mensagem lida
LAST_MESSAGE_ID_FILE = f'last_message_id_{CHANNEL_IDENTIFIER.replace("@", "")}.txt'
# --- Fim das Configurações ---

def get_last_message_id():
    """Lê o ID da última mensagem processada de um arquivo."""
    if os.path.exists(LAST_MESSAGE_ID_FILE):
        with open(LAST_MESSAGE_ID_FILE, 'r') as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0 # Retorna 0 se o arquivo estiver vazio ou com formato inválido
    return 0 # Retorna 0 se o arquivo não existir

def save_last_message_id(message_id):
    """Salva o ID da última mensagem processada em um arquivo."""
    with open(LAST_MESSAGE_ID_FILE, 'w') as f:
        f.write(str(message_id))

async def fetch_new_messages():
    # O nome da sessão será derivado do número de telefone.
    # Você pode especificar um nome de sessão diferente se desejar: client = TelegramClient('minha_sessao', API_ID, API_HASH)
    client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

    print(f"Iniciando script em: {datetime.datetime.now()}")

    try:
        await client.connect()

        if not await client.is_user_authorized():
            print("Autenticação necessária. Por favor, execute o script interativamente uma vez.")
            await client.send_code_request(PHONE_NUMBER)
            try:
                code = input('Digite o código recebido: ')
                try:
                    await client.sign_in(PHONE_NUMBER, code)
                except Exception as e:
                    if "password" in str(e).lower():
                        # Se precisar de senha de verificação em duas etapas
                        password = input('Digite sua senha de verificação em duas etapas: ')
                        await client.sign_in(password=password)
                    else:
                        raise e
            except Exception as e:
                print(f"Falha na autenticação: {e}")
                return # Sai se a autenticação falhar
            print("Autenticado com sucesso!")


        channel_entity = await client.get_entity(CHANNEL_IDENTIFIER)
        print(f"Acessando o canal: {getattr(channel_entity, 'title', CHANNEL_IDENTIFIER)}")

        last_processed_id = get_last_message_id()
        print(f"ID da última mensagem processada anteriormente: {last_processed_id}")

        new_messages_found = False
        current_max_id = 0 # Para guardar o ID da mensagem mais recente desta execução

        # Usamos min_id para buscar mensagens MAIS RECENTES que o last_processed_id
        # Iteramos em lotes para garantir que não percamos mensagens se houver muitas
        offset_id = 0
        limit = 100 # Processar em lotes de 100

        all_messages_batch = []

        while True:
            history = await client(GetHistoryRequest(
                peer=channel_entity,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0, # max_id=0 para pegar as mais recentes a partir do offset_id
                min_id=last_processed_id, # Pega mensagens com ID maior que este
                hash=0
            ))

            if not history.messages:
                break # Sem mais mensagens novas

            batch_messages = []
            for message in history.messages:
                if message.id > last_processed_id:
                    batch_messages.append(message)
                    if message.id > current_max_id:
                        current_max_id = message.id
                    new_messages_found = True

            # As mensagens vêm da mais recente para a mais antiga no lote.
            # Para processar da mais antiga para a mais recente, invertemos.
            all_messages_batch.extend(reversed(batch_messages))

            if len(history.messages) < limit: # Se recebemos menos que o limite, é o último lote
                break

            # Define o offset_id para a mensagem mais antiga do lote atual para paginar para trás
            # No entanto, como estamos usando min_id, o comportamento é pegar mensagens *após* min_id.
            # Se quisermos pegar tudo e depois filtrar, podemos remover min_id e paginar
            # de forma diferente, mas para "novas mensagens", min_id é eficiente.
            # Neste loop, como estamos buscando mensagens *depois* de last_processed_id,
            # e as mensagens vêm em ordem decrescente de ID, não precisamos ajustar offset_id
            # de forma complexa. O min_id já cuida da filtragem.
            # O loop vai parar quando não houver mais mensagens ou quando history.messages for vazio.
            # Para garantir que pegamos todas as mensagens se houver mais de 'limit' mensagens novas:
            # precisamos reavaliar a lógica de paginação com min_id.
            # A forma mais simples com min_id é pegar um lote grande.
            # Ou, iterar pegando as mais recentes e parar quando message.id <= last_processed_id.

            # Correção para paginação buscando mensagens mais recentes que min_id:
            # O `min_id` na GetHistoryRequest faz com que a API retorne apenas mensagens com ID > min_id.
            # As mensagens são retornadas da mais recente para a mais antiga.
            # Se houver mais de `limit` mensagens, precisamos continuar.
            # O `offset_id` aqui seria o ID da última mensagem recebida no lote anterior
            # para continuar buscando mensagens *mais antigas* a partir daquele ponto,
            # mas ainda respeitando o `min_id`.
            if not history.messages or history.messages[-1].id <= last_processed_id:
                break
            offset_id = history.messages[-1].id


        if not new_messages_found:
            print("Nenhuma mensagem nova desde a última verificação.")
        else:
            print(f"Encontradas {len(all_messages_batch)} novas mensagens.")
            for message in all_messages_batch: # Processa da mais antiga para a mais nova
                print(f"\n--- Nova Mensagem ---")
                print(f"ID: {message.id}")
                print(f"Data: {message.date.strftime('%Y-%m-%d %H:%M:%S')}")
                if hasattr(message.sender, 'username') and message.sender.username:
                    print(f"Remetente: @{message.sender.username}")
                elif hasattr(message.sender, 'title'): # Se for um canal postando em nome de outro
                    print(f"Remetente (Canal): {message.sender.title}")
                else:
                    print(f"Remetente ID: {message.sender_id}")

                if message.message:
                    print(f"Texto: {message.message[:200]}") # Primeiros 200 caracteres
                if message.media:
                    print(f"Mídia: Sim ({type(message.media).__name__})")
                if message.reactions:
                    reaction_counts = [f"{r.emoticon}({r.count})" for r in message.reactions.results]
                    print(f"Reações: {', '.join(reaction_counts)}")

                # Aqui você pode adicionar a lógica para processar a mensagem:
                # - Salvar em um banco de dados
                # - Enviar para outro lugar
                # - Analisar o conteúdo, etc.

            # Salva o ID da mensagem mais recente processada nesta execução
            if current_max_id > last_processed_id:
                save_last_message_id(current_max_id)
                print(f"\nID da última mensagem processada atualizado para: {current_max_id}")

    except ConnectionError:
        print("Erro de conexão. Verifique sua internet ou as configurações do Telegram.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        import traceback
        traceback.print_exc() # Imprime o traceback completo para depuração
    finally:
        if client.is_connected():
            await client.disconnect()
            print("Cliente desconectado.")
        print(f"Script finalizado em: {datetime.datetime.now()}\n")

if __name__ == '__main__':
    # Para Telethon funcionar corretamente em alguns ambientes (como scripts agendados),
    # pode ser necessário definir um loop de eventos específico se o padrão não funcionar.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_new_messages())
    #asyncio.run(fetch_new_messages())