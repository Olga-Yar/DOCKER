from django.contrib import admin

from users.models import UserCustom


@admin.register(UserCustom)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'avatar', 'phone', 'chat_id', 'telegram', 'role'
    )
