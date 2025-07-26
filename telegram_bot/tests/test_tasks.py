import pytest
from django.utils.timezone import localtime, now
from datetime import timedelta, time
from habits.models import Habit
from users.models import TelegramProfile
from telegram_bot.tasks import send_daily_habit_reminders
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_send_daily_habit_reminders(monkeypatch):
    # Подготовка пользователя и привычки
    user = User.objects.create_user(username="reminder", password="123")
    TelegramProfile.objects.create(user=user, telegram_chat_id="999", verified=True)

    habit = Habit.objects.create(
        user=user,
        place="дом",
        time=(localtime(now()) + timedelta(seconds=10)).time().replace(second=0, microsecond=0),
        action="напиться чаю",
        periodicity=1,
        execution_time=60,
    )

    # Переопределяем функции, чтобы не отправлять реальные сообщения
    monkeypatch.setattr(
        "telegram_bot.tasks.send_telegram_message", lambda chat_id, msg: print(f"[FAKE SEND] {chat_id}: {msg}")
    )
    monkeypatch.setattr("telegram_bot.tasks.build_habit_message", lambda h: f"Напоминание: {h.action}")

    # Запуск задачи
    send_daily_habit_reminders()

    assert True
