from io import BytesIO
from telethon import events
import telethon.client
import qrcode

async def qr(client: telethon.TelegramClient, event: events.NewMessage.Event):
    if not event.text.startswith('.qr'):
        return
    text = event.text[3:].strip()
    chat_id = event.chat_id

    await event.delete()

    img = qrcode.make(text)
    bio = BytesIO()
    bio.name = 'image.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    await client.send_file(chat_id, bio)