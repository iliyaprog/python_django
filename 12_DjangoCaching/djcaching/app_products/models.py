from django.db import models
from main_page.models import Product
from django.utils.translation import gettext_lazy as _


class PromotionsAndOffers(models.Model):
    description = models.CharField(max_length=100, verbose_name=_('descriptions'))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


