import pytest
from datetime import time
from habits.models import Habit
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_cannot_have_related_habit_and_reward():
    user = User.objects.create_user(username="test", password="123")
    pleasant = Habit.objects.create(
        user=user,
        place="дом",
        time=time(10, 0),
        action="чай",
        is_pleasant=True,
        execution_time=60,
        periodicity=1,
    )

    habit = Habit(
        user=user,
        place="офис",
        time=time(11, 0),
        action="работа",
        related_habit=pleasant,
        reward="кофе",
        execution_time=60,
        periodicity=1,
    )

    with pytest.raises(ValidationError) as excinfo:
        habit.clean()

    assert "Нельзя одновременно указать и связанную привычку, и вознаграждение." in str(excinfo.value)


def test_execution_time_limit():
    user = User.objects.create_user(username="test", password="123")

    habit = Habit(
        user=user,
        place="офис",
        time=time(9, 0),
        action="доклад",
        execution_time=150,  # превышает лимит
        periodicity=1,
    )

    with pytest.raises(ValidationError) as excinfo:
        habit.clean()

    assert "Время выполнения не должно превышать 120 секунд." in str(excinfo.value)


def test_pleasant_habit_cannot_have_reward_or_related():
    user = User.objects.create_user(username="test", password="123")

    pleasant = Habit(
        user=user,
        place="парк",
        time=time(8, 0),
        action="прогулка",
        is_pleasant=True,
        reward="мороженое",
        execution_time=60,
        periodicity=1,
    )

    with pytest.raises(ValidationError) as excinfo:
        pleasant.clean()

    assert "Приятная привычка не может иметь вознаграждение или связанную привычку." in str(excinfo.value)


def test_periodicity_must_be_between_1_and_7():
    user = User.objects.create_user(username="test", password="123")

    habit = Habit(
        user=user,
        place="дом",
        time=time(12, 0),
        action="чтение",
        execution_time=60,
        periodicity=10,  # недопустимо
    )

    with pytest.raises(ValidationError) as excinfo:
        habit.clean()

    assert "Периодичность должна быть от 1 до 7 дней." in str(excinfo.value)


