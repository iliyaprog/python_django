from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from logic_library.models import BookModel, AuthorModel
from app_book.serializers import BookSerializer
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from app_book.paginator import BookResultsSetPagination
from django.core.paginator import Paginator


class BookViews(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Класс для представления API книг"""
    serializer_class = BookSerializer
    pagination_class = BookResultsSetPagination

    def get_queryset(self):
        """Функция фильтрует книги по названию, автору или по количеству страниц"""
        queryset = BookModel.objects.all()
        item_name = self.request.query_params.get('name')
        item_author = self.request.query_params.get('author')

        item_count_list = self.request.query_params.get('count_list')
        gte_item_count_list = self.request.query_params.get('gte_count_list')
        lte_item_count_list = self.request.query_params.get('lte_count_list')
        pages_filter_rules = (
            ('count_list', item_count_list),
            ('count_list__gte', gte_item_count_list),
            ('count_list__lte', lte_item_count_list),
        )
        try:
            pages_filter_rules = next(filter(lambda value: value[1] is not None, pages_filter_rules))
        except StopIteration:
            pages_filter_rules = None

        if pages_filter_rules is not None:
            pages_filter_rules = dict((pages_filter_rules,))
            queryset = queryset.filter(**pages_filter_rules)

        if item_name:
            queryset = queryset.filter(name=item_name)
        if item_author:
            list_queryset = []
            queryset_author = AuthorModel.objects.filter(surname=item_author)
            for i_book in queryset:
                if i_book.author in queryset_author:
                    list_queryset.append(i_book)
            queryset = list_queryset

        return queryset

    def get(self, request):
        """Функция для представления книг"""
        return self.list(request)

    def post(self, request, format=None):
        """Функция для получения новой книги"""
        return self.create(request)


class BooKDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о книге,
    а так же для редактирования и удаления"""
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)