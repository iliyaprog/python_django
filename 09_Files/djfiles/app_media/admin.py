from django.contrib import admin
from app_media.models import FeedFile, Feed


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_ap', 'user', 'text')


admin.site.register(Feed, FileAdmin)
