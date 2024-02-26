from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['display_user', 'display_birth']
    raw_id_fields = ['user']

    def display_user(self, obj):
        return f"{obj.user}"
    display_user.short_description = 'Автор'

    def display_birth(self, obj):
        return f"{obj.date_birth}"
    display_birth.short_description = 'День рождения'
