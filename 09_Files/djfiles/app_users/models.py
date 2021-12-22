from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    profile_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.id}. {self.user}'
