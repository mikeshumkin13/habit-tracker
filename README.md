# 📌 Habit Tracker — трекер привычек

## 📖 Описание проекта

Трекер привычек — это Django-приложение, позволяющее пользователю:
- создавать полезные и приятные привычки;
- назначать периодичность и награды;
- получать напоминания в Telegram;
- отслеживать выполнение.

## 🔧 Технологии

- Python 3.12
- Django 5.2
- Django REST Framework
- Celery + Redis
- PostgreSQL / SQLite
- Telegram Bot API
- drf-spectacular (Swagger, Redoc)
- Pytest

## 🚀 Запуск

1. Установите зависимости:


poetry install

2. Создайте .env файл и добавьте:
TELEGRAM_BOT_TOKEN=ваш_токен

3. Запуск Redis и Celery:

Терминал 1

redis-server

Терминал 2

poetry run celery -A config worker -l info

4. Запуск сервера:

poetry run python manage.py runserver


# Документация

Swagger UI

Redoc

# Тесты

Запуск тестов:

poetry run pytest



# Автор:
mikeshumkin13

https://github.com/mikeshumkin13/habit-tracker/tree/feature/models_and_auth

Проект выполнен в рамках курсовой работы по профессии Python-разработчик в SkyPro.
