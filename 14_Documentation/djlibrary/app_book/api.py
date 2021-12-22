from rest_framework import viewsets
from logic_library.models import BookModel
from app_book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Класс для описания API модели книги"""
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer