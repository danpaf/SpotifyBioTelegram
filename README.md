
# SpotifyBioTelegram

## Описание проекта:

SpotifyBioTelegram - это юзербот для Telegram, который автоматически обновляет ваше био в Telegram, отображая текущий воспроизводимый трек из Spotify. С помощью данного проекта вы сможете добавить динамическое содержание в свой профиль в Telegram, позволяя вашим контактам узнавать о текущей музыке, которую вы слушаете.

## Основные возможности:

- Получение информации о текущем воспроизводимом треке из Spotify.
- Автоматическое обновление вашего био в Telegram с информацией о треке.
- Поддержка настраиваемых параметров авторизации Spotify и Telegram.

## Использование:

1. Установите все необходимые зависимости, запустив `pip install -r requirements.txt`.
2. Создайте файл `config.json` со следующей структурой:

```
{
  "spotify": {
    "client_id": "YOUR_SPOTIFY_CLIENT_ID",
    "client_secret": "YOUR_SPOTIFY_CLIENT_SECRET",
    "redirect_uri": "YOUR_SPOTIFY_REDIRECT_URI"
  },
  "telegram": {
    "api_id": "YOUR_TELEGRAM_API_ID",
    "api_hash": "YOUR_TELEGRAM_API_HASH"
  }
}

```

1. Зарегистрируйте свое приложение в Spotify API, чтобы получить `client_id`, `client_secret` и `redirect_uri` на [SpotifyDev website](https://developer.spotify.com).
2. Получите `api_id` и `api_hash` от Telegram, создав приложение на [Telegram's website](https://my.telegram.org/apps).
3. Запустите `python main.py` для запуска приложения.