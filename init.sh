#!/bin/bash

# Переходим в папку config
cd "$(dirname "$0")/config" || exit 1

# Запрашиваем данные у пользователя
read -p "Введите новый API ID: " api_id
read -p "Введите новый API Hash: " api_hash

# Генерируем новый config.py
cat > config.py << EOF
API_ID = $api_id
API_HASH = "$api_hash"
EOF

echo "Конфиг успешно обновлён!"