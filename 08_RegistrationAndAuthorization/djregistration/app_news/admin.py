from django.contrib import admin
from app_news import models
from app_news.forms import NewsCommentForm
from app_news.models import News, Comment, CommentNews
from django.core.exceptions import PermissionDenied


class CommentInLine(admin.TabularInline):
    model = CommentNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'flag_activate', 'tag']
    list_filter = ['flag_activate', 'tag']
    inlines = [CommentInLine]

    actions = ['flag_is_activate', 'flag_is_not_activate']

    def flag_is_activate(self, request, queryset):
        if not request.user.has_perm('app_news.can_publish'):
            raise PermissionDenied()
        queryset.update(flag_activate=True)

    def flag_is_not_activate(self, request, queryset):
        if not request.user.has_perm('app_news.can_publish'):
            raise PermissionDenied()
        queryset.update(flag_activate=False)

    flag_is_activate.short_description = 'Перевести в статус Активно'
    flag_is_not_activate.short_description = 'Перевести в статус Неактивно'


class CommentAdmin(admin.ModelAdmin):
    def get_text(self, object):
        try:
            ended_text = object.text[:15] + '...'
            return ended_text
        except:
            ended_text = object.text + '...'
            return ended_text

    get_text.short_description = 'text'

    list_display = ['news', 'author', 'get_text']
    list_filter = ['author']

    actions = ['delete_comment']

    def delete_comment(self, request, queryset):
        queryset.update(text='Удалено администратором', author='Admin')

    delete_comment.short_description = 'Удалить комментарии'


class CommentNewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentNews, CommentNewsAdmin)
