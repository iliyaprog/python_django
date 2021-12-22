from django.db import models
from django.utils.translation import gettext as _

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='files/')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title
