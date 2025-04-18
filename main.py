import os
import importlib
import inspect
from telethon import TelegramClient, events
from config.config import api_id, api_hash

try:
    client = TelegramClient('test', api_id, api_hash)
    print('Бот запущен')

    async def load_commands():
        utils_dir = 'utils'
        commands = set()
        outgoing_commands = set()

        for filename in os.listdir(utils_dir):
            if filename.endswith('.py') and not filename.startswith('__') and not filename.startswith('out_'):
                module_name = filename[:-3]
                command_name = f'.{module_name}'

                if command_name in commands:
                    continue

                try:
                    module = importlib.import_module(f'{utils_dir}.{module_name}')

                    for name, obj in inspect.getmembers(module):
                        if inspect.iscoroutinefunction(obj) and not name.startswith('_'):
                            
                            @client.on(events.NewMessage(pattern=rf'\{command_name}(?:\s|$)'))
                            async def handler(event, func=obj):
                                try:
                                    if 'client' in inspect.signature(func).parameters:
                                        await func(client, event)
                                    else:
                                        await func(event)
                                except Exception as e:
                                    print(f'Ошибка выполнения {command_name}: {e}')

                            commands.add(command_name)
                            print(f'Команда {command_name} загружена')
                            break

                except Exception as e:
                    print(f'Ошибка загрузки {filename}: {e}')
            elif filename.startswith('out_'):
                module_name = filename[:-3]
                command_name = f'.{module_name}'

                if command_name in outgoing_commands:
                    continue

                try:
                    module = importlib.import_module(f'{utils_dir}.{module_name}')

                    for name, obj in inspect.getmembers(module):
                        if inspect.iscoroutinefunction(obj) and not name.startswith('_'):
                            
                            @client.on(events.NewMessage(outgoing=True))
                            async def outgoing_handler(event, func=obj):
                                try:
                                    if 'client' in inspect.signature(func).parameters:
                                        await func(client, event)
                                    else:
                                        await func(event)
                                except Exception as e:
                                    print(f'Ошибка выполнения {command_name}: {e}')

                            outgoing_commands.add(command_name)
                            print(f'Текстовая команда {command_name} загружена')
                            break

                except Exception as e:
                    print(f'Ошибка загрузки {filename}: {e}')

        return outgoing_commands

    async def main():
        await load_commands()
        await client.run_until_disconnected()

    if __name__ == '__main__':
        with client:
            client.loop.run_until_complete(main())

except KeyboardInterrupt:
    print('Скрипт остановлен')