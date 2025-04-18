#!/bin/bash

# Переход в директорию скрипта
cd "$(dirname "$0")"

# Проверка наличия Python
if ! command -v python3 &> /dev/null
then
    echo "Python3 не установлен"
    pkg update
    pkg upgrade -y
    pkg install python
fi

# проверка наличия uv
if ! command -v uv &> /dev/null
then
    echo "uv не установлен"
    pkg install uv
fi

# Проверка зависимостей
uv sync
