from django.urls import path
from . import views
from .views import NewsFormView, DetailNewsView, UpgreateNewsView, AnotherLoginView, CreateNewsView
from app_news.views import login_view, logout_view

urlpatterns = [
    path('', NewsFormView.as_view(), name='title_news'),
    path('detail_news/<int:profile_id>', DetailNewsView.as_view(), name='detail_news'),
    path('upgreate_news/<int:profile_id>', UpgreateNewsView.as_view(), name='upgreate_news'),
    path('create_news', CreateNewsView.as_view(), name='create_news'),
    path('login/', login_view, name='login'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('logout/', logout_view, name='logout'),
]
