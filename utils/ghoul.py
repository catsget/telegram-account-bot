from asyncio import sleep
from telethon import events
import telethon.client

async def ghoul_spam(client: telethon.client.TelegramClient, event: events.NewMessage):
   await event.delete()
   i = 1000
   while i != -1:
      await client.send_message(event.chat_id, f'**{i} - 7 = {i - 7}**')
      i -= 7
      sleep(0.1)