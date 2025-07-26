from habits.models import Habit


def build_habit_message(habit: Habit) -> str:
    return (
        f"⏰ Напоминание!\n"
        f"Место: <b>{habit.place}</b>\n"
        f"Действие: <b>{habit.action}</b>\n"
        f"Время: <b>{habit.time.strftime('%H:%M')}</b>"
    )


