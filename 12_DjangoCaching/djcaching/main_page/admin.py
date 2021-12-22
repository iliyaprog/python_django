from django.contrib import admin
from main_page.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Product, ProductAdmin)