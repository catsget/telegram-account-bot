from asyncio import sleep
from telethon import events

heartParts = [
    '░░░░░░░░░░░░\n'
    '░░▄███▄███▄░\n',
    '░░█████████░\n',
    '░░░▀█████▀░░\n',
    '░░░░░▀█▀░░░░\n',
    'это тебе :3'
]

async def heart(event: events.NewMessage):
    for i in range(21):
        newStr = f'ЗАГРУЗКА.. {i*5}%'
        await event.edit(newStr)
        await sleep(0.2)
    newStr = ''
    await event.edit('ㅤㅤㅤㅤㅤㅤㅤㅤ')
    for i in heartParts:
        await sleep(1)
        newStr += i
        await event.edit(newStr)