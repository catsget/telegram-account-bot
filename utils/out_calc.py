from re import findall, sub
from telethon import events
from utils.external.calculate import calculate_expression

async def calc(event: events.NewMessage):
    text = event.text
    if not text:
        return
    
    if '.calc' in text:
        pattern = r'\.calc\s+([^\n]+)'
        matches = findall(pattern, text)
        if matches:
            expr = matches[0].strip()
            result = calculate_expression(expr)
            new_text = sub(pattern, result, text, count=1)

            await event.edit(new_text)