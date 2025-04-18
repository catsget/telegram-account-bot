#!/bin/bash

# Переход в директорию скрипта (если нужно)
cd "$(dirname "$0")"

# Проверка наличия Python
if ! command -v python3 &> /dev/null
then
    echo "Python3 не установлен"
    pkg update
    pkg upgrade -y
    pkg install python
fi

if ! command -v uv &> /dev/null
then
    echo "python uv не установлен"
    pip install uv

# Проверка зависимостей
uv sync

# Запуск бота
uv run main.py