from django.urls import path
from app_book.views import BookViews


urlpatterns = [
    path('books/', BookViews.as_view(), name='book_list')
]