from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Автора'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.user.username
