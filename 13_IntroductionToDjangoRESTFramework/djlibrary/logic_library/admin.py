from django.contrib import admin
from logic_library.models import AuthorModel, BookModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'date_of_birth']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'date_of_release', 'isbn', 'count_list']


admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(BookModel, BookAdmin)