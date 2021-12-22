from django.urls import path
from app_book.views import BookViews, BooKDetail


urlpatterns = [
    path('books/', BookViews.as_view(), name='book_list'),
    path('books/<int:pk>', BooKDetail.as_view(), name='book_detail')
]