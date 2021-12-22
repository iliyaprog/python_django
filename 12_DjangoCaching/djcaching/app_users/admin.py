from django.contrib import admin
from app_users.models import Avatar, Bonus, ShoppingList


class AvatarAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

class BonusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bonus']

class ShopListAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'shop_list']

admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(ShoppingList, ShopListAdmin)
