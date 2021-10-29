from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ProfileModel(models.Model):
    profile_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_phone = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, blank=True)
    data_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.id}. {self.user} ({self.city}, {self.num_phone})'