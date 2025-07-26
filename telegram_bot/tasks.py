from celery import shared_task
from django.utils.timezone import localtime, now
from datetime import timedelta
from habits.models import Habit
from telegram_bot.bot import send_telegram_message
from telegram_bot.services import build_habit_message


@shared_task
def send_daily_habit_reminders():
    current_dt = localtime(now())
    weekday = current_dt.weekday()
    current_time = current_dt.time().replace(second=0, microsecond=0)

    # Устанавливаем окно ±1 минута
    time_window_start = (current_dt - timedelta(minutes=1)).time()
    time_window_end = (current_dt + timedelta(minutes=1)).time()

    print(f"[DEBUG] Проверка времени: {current_time}, день недели: {weekday}")
    print(f"[DEBUG] Окно времени: {time_window_start} — {time_window_end}")

    # Получаем все привычки и фильтруем вручную
    all_habits = Habit.objects.all()
    matching_habits = []

    for habit in all_habits:
        habit_time = habit.time.replace(second=0, microsecond=0)
        if time_window_start <= habit_time <= time_window_end:
            if habit.periodicity and (weekday % habit.periodicity == 0):
                matching_habits.append(habit)

    print(f"[DEBUG] Найдено привычек: {len(matching_habits)}")

    for habit in matching_habits:
        user = habit.user
        tg_profile = getattr(user, 'telegram_profile', None)

        if tg_profile and tg_profile.telegram_chat_id:
            message = build_habit_message(habit)
            send_telegram_message(tg_profile.telegram_chat_id, message)

    print(f"[DEBUG] Всего привычек в базе: {Habit.objects.count()}")
    print(f"[DEBUG] Подходящие привычки: {matching_habits}")


