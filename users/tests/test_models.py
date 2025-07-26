import pytest
from users.models import TelegramProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_telegram_profile():
    user = User.objects.create_user(username="user", password="123")
    profile = TelegramProfile.objects.create(user=user, telegram_chat_id="123456789", verified=True)

    assert profile.user == user
    assert profile.telegram_chat_id == "123456789"
    assert profile.verified is True
    assert str(profile) == f"Telegram профиль пользователя {user.email}"


