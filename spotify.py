import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Чтение конфигурационного файла
with open('config.json') as config_file:
    config = json.load(config_file)

# Установка параметров авторизации
scope = "user-read-currently-playing"
username = "your_username"
spotify_config = config['spotify']
client_id = spotify_config['client_id']
client_secret = spotify_config['client_secret']
redirect_uri = spotify_config['redirect_uri']

def get_track_name():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username, client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))

    # Получение текущего воспроизводимого трека
    current_track = sp.current_user_playing_track()

    # Извлечение названия трека
    if current_track is not None and "item" in current_track:
        track_name = current_track["item"]["name"]
        artist_name = current_track["item"]["artists"][0]["name"]
        print("Текущий трек:", track_name, "\n",f"Артист: {artist_name}")
    else:
        print("Сейчас не воспроизводится ни один трек.")
    return (track_name,artist_name)
