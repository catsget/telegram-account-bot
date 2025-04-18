from telethon import events

async def flip(event: events.NewMessage.Event):
    if not event.text.startswith('.flip'):
        return
    
    text = event.text[5:].strip()  # Убираем ".flip"
    
    flipped = text[::-1]  # Переворачиваем строку
    await event.edit(flipped)