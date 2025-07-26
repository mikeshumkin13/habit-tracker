from django.conf import settings
from django.db import models


class TelegramProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="telegram_profile")
    telegram_chat_id = models.CharField(max_length=100, verbose_name="Telegram Chat ID")
    verified = models.BooleanField(default=False, verbose_name="Подтвержден")

    def __str__(self):
        return f"Telegram профиль пользователя {self.user.email}"
