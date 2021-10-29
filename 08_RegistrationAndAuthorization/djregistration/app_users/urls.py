from django.urls import path
# from . import views
# from .views import NewsFormView, CreateNewsView, DetailNewsView, UpgreateNewsView, AnotherLoginView, AnotherLogoutView
from app_users.views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
]