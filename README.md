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

# Структура проекта

.
├── README.md
├── config
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── celery.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── habits
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── serializers.cpython-312.pyc
│   │   ├── tasks.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── test_models.cpython-312-pytest-8.4.1.pyc
│   │   └── test_models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── telegram_bot
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── bot.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── services.cpython-312.pyc
│   │   ├── tasks.cpython-312.pyc
│   │   └── tests.cpython-312-pytest-8.4.1.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── bot.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── services.py
│   ├── tasks.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── test_tasks.cpython-312-pytest-8.4.1.pyc
│   │   └── test_tasks.py
│   └── views.py
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── admin.cpython-312.pyc
    │   ├── apps.cpython-312.pyc
    │   ├── models.cpython-312.pyc
    │   ├── serializers.cpython-312.pyc
    │   ├── tests.cpython-312-pytest-8.4.1.pyc
    │   ├── urls.cpython-312.pyc
    │   └── views.cpython-312.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-312.pyc
    │       └── __init__.cpython-312.pyc
    ├── models.py
    ├── tests
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   └── test_models.cpython-312-pytest-8.4.1.pyc
    │   └── test_models.py
    └── views.py


# Тесты

Запуск тестов:

poetry run pytest



# Автор:
mikeshumkin13

https://github.com/mikeshumkin13/habit-tracker/tree/feature/models_and_auth

Проект выполнен в рамках курсовой работы по профессии Python-разработчик в SkyPro.
