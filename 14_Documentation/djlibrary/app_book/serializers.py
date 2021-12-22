from logic_library.models import BookModel
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """Класс сериализатора который описывает модель книги"""
    class Meta:
        model = BookModel
        fields = ['id', 'author', 'name', 'date_of_release', 'isbn', 'count_list']
