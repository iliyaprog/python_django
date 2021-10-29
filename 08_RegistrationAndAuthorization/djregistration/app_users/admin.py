from django.contrib import admin
from app_users.models import ProfileModel


class UserAdmin(admin.ModelAdmin):

    def upper_case_name(self, obj):
        return obj.user.first_name, obj.user.last_name

    upper_case_name.short_description = 'user'

    list_display = ('upper_case_name', 'num_phone', 'city', 'data_of_birth')


admin.site.register(ProfileModel, UserAdmin)
