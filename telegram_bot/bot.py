import requests
from django.conf import settings


def send_telegram_message(chat_id: str, text: str) -> None:
    token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")


