from django.urls import path

from logic_library.views import main_page_view, DetailBook, DetailAuthor

urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('detail_book/<int:book_id>', DetailBook.as_view(), name='detail_book'),
    path('detail_author/<int:author_id>', DetailAuthor.as_view(), name='detail_author'),
    ]