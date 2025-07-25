from habits.models import Habit


def build_habit_message(habit: Habit) -> str:
    return f"⏰ Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"


