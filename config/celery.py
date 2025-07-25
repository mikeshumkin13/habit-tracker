import os
from celery import Celery

# Указываем настройки Django как точку входа
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Инициализируем Celery
app = Celery('habit_tracker')

# Подтягиваем настройки Celery из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживать задачи из всех app'ов
app.autodiscover_tasks()


