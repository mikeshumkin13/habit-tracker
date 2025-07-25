from habits.models import Habit
import requests
from django.conf import settings




def build_habit_message(habit: Habit) -> str:
    return f"⏰ Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"



def send_telegram_message(chat_id: str, text: str) -> None:
    print(f"📤 Отправляем сообщение в Telegram chat_id={chat_id}: {text}")  # отладка

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }

    response = requests.post(url, data=payload)
    print(f" Ответ Telegram API: {response.status_code} — {response.text}")  # отладка


