from logic_library.models import BookModel
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'author', 'name', 'date_of_release', 'isbn', 'count_list']
