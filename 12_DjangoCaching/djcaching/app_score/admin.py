from django.contrib import admin
from app_score.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'score']


admin.site.register(Shop, ShopAdmin)
