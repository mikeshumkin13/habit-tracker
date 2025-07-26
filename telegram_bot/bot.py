import requests
from django.conf import settings


def send_telegram_message(chat_id: str, text: str) -> None:
    print(f"[DEBUG] Пытаемся отправить сообщение в чат {chat_id}")
    print(f"[DEBUG] Сообщение: {text}")

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print(f"[DEBUG] Успешно отправлено! Статус: {response.status_code}")
    except requests.RequestException as e:
        print(f"[ERROR] Ошибка при отправке в Telegram: {e}")


