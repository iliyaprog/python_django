from django.contrib import admin
from app_products.models import PromotionsAndOffers

class AdminOffer(admin.ModelAdmin):
    list_display = ['id', 'description', 'product']


admin.site.register(PromotionsAndOffers, AdminOffer)
