from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='files')
    avatar = models.ImageField(upload_to='files/')


class Bonus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_list = models.TextField(default='')
