from rest_framework import viewsets
from logic_library.models import AuthorModel
from app_author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """Класс для описания API модели авторов"""
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
