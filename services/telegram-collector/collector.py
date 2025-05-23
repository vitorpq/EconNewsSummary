#%% services/telegram_collector/collector.py
from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from datetime import datetime, timedelta
import asyncio # Import asyncio
import json

from dotenv import load_dotenv
from pathlib import Path
import os
#%%
# Sempre procura o .env na raiz
load_dotenv('/Users/vitor/Projects/NewsSummaryV2/.env')

#%%
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
CHANNEL_IDENTIFIER = os.getenv("TELEGRAM_CHANNEL")
SESSION_NAME = os.getenv("TELEGRAM_SESSION_NAME")

async def get_all_yesterday_messages():
    today = datetime.now()
    is_monday = today.weekday() == 0  # 0 representa segunda-feira
    
    if is_monday:
        # Para segunda-feira, buscamos mensagens de sexta e do dia atual até 12h
        friday = today - timedelta(days=3)  # 3 dias antes de segunda é sexta
        friday_date = friday.date()
        today_date = today.date()
        texts_for_period = []
        
        async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
            channel_entity = await client.get_entity(CHANNEL_IDENTIFIER)
            
            async for msg in client.iter_messages(channel_entity, limit=None):
                current_msg_date = msg.date.date()
                current_msg_time = msg.date.time()
                
                # Verifica se a mensagem é de sexta ou de hoje até 12h
                if (current_msg_date == friday_date) or \
                   (current_msg_date == today_date and current_msg_time.hour < 12):
                    if msg.text:
                        texts_for_period.append(msg.text)
                elif current_msg_date < friday_date:
                    break
                    
        return texts_for_period
    else:
        # Comportamento original para outros dias
        yesterday_obj = today - timedelta(days=1)
        yesterday_date_val = yesterday_obj.date()
        texts_for_yesterday = []

        async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
            channel_entity = await client.get_entity(CHANNEL_IDENTIFIER)
            
            async for msg in client.iter_messages(channel_entity, limit=None):
                current_msg_date = msg.date.date()

                if current_msg_date == yesterday_date_val:
                    if msg.text:
                        texts_for_yesterday.append(msg.text)
                elif current_msg_date < yesterday_date_val:
                    break 
                    
        return texts_for_yesterday

async def main():
    """Main function to orchestrate the script."""
    texts = await get_all_yesterday_messages()
    print(json.dumps(texts, ensure_ascii=False))

if __name__ == "__main__":
    # Run the main async function
    asyncio.run(main())
