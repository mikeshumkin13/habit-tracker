from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from telegram_bot.bot import send_telegram_message
from telegram_bot.services import build_habit_message


@shared_task
def send_daily_habit_reminders():
    now = timezone.now()
    current_time = now.time()
    weekday = now.weekday()  # Пн=0 ... Вс=6

    # Выбираем привычки, у которых сегодня день по периодичности
    habits = Habit.objects.filter(
        time__hour=current_time.hour,
        time__minute=current_time.minute
    )

    for habit in habits:
        if habit.periodicity and (weekday % habit.periodicity == 0):
            user = habit.user
            tg_profile = getattr(user, 'telegram_profile', None)

            if tg_profile and tg_profile.telegram_chat_id:
                message = build_habit_message(habit)
                send_telegram_message(tg_profile.telegram_chat_id, message)



