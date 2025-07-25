from django.contrib import admin
from .models import TelegramProfile

@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram_chat_id', 'verified')
    search_fields = ('user__email', 'telegram_chat_id')


