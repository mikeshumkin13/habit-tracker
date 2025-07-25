from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from users.models import TelegramProfile
import requests


@shared_task
def send_habit_reminder():
    now = timezone.now()
    current_time = now.time()

    habits = Habit.objects.filter(time__hour=current_time.hour, time__minute=current_time.minute)

    for habit in habits:
        user = habit.user
        tg_profile = getattr(user, 'telegram_profile', None)

        if tg_profile and tg_profile.telegram_chat_id:
            message = f"⏰ Напоминание: {habit.action} в {habit.place}"
            send_telegram_message(tg_profile.telegram_chat_id, message)


def send_telegram_message(chat_id: str, text: str):
    from django.conf import settings

    token = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")



