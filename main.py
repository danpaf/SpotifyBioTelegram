import json
import logging
from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest

import spotify

with open('config.json') as config_file:
    config = json.load(config_file)

# Конфигурация API-ключа
telegram_config = config['telegram']
api_id = telegram_config['api_id']
api_hash = telegram_config['api_hash']

# Настройка логирования
logging.basicConfig(level=logging.WARNING)

# Создание экземпляра клиента Telegram
client = TelegramClient('userbot_session', api_id, api_hash)
client.start()


def update_bio():
    print('asd')
    track = spotify.get_track_name()  # Замените на свое новое био
    new_bio = f"Сейчас играет: {track[0]} Артист: {track[1]}"
    client(UpdateProfileRequest(about=new_bio))


update_bio()

# Запуск обработки событий
client.run_until_disconnected()
