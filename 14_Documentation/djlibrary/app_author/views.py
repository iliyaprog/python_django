from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from logic_library.models import AuthorModel
from app_author.serializers import AuthorSerializer
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from app_author.paginator import AuthorResultsSetPagination
from django.core.paginator import Paginator


class AuthorViews(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Класс для представления API авторов"""
    serializer_class = AuthorSerializer
    pagination_class = AuthorResultsSetPagination

    def get_queryset(self):
        """Функция для получения авторов по фамилии"""
        queryset = AuthorModel.objects.all()
        author_surname = self.request.query_params.get('surname')
        if author_surname:
            queryset = queryset.filter(surname=author_surname)
        return queryset

    def get(self, request):
        """Функция для представления авторов"""
        return self.list(request)

    def post(self, request, format=None):
        """Функция для получения нового автора"""
        return self.create(request)


class AuthorDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о книге,
    а так же для редактирования и удаления"""
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
