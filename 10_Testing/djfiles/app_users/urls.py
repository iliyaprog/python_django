from django.urls import path
from app_users.views import register_view, edit_view, password_recovery

urlpatterns = [
    path('register/', register_view, name='register'),
    path('edit_user', edit_view, name='edit_user'),
    path('password_recovery', password_recovery, name='recovery')
]