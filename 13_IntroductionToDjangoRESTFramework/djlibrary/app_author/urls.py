from django.urls import path
from app_author.views import AuthorViews


urlpatterns = [
    path('authors/', AuthorViews.as_view(), name='author_list')
]