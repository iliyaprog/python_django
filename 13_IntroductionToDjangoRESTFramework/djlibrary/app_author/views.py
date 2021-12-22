from rest_framework.mixins import ListModelMixin, CreateModelMixin
from logic_library.models import AuthorModel
from app_author.serializers import AuthorSerializer
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from app_author.paginator import AuthorResultsSetPagination
from django.core.paginator import Paginator


class AuthorViews(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = AuthorSerializer
    pagination_class = AuthorResultsSetPagination

    def get_queryset(self):
        queryset = AuthorModel.objects.all()
        author_surname = self.request.query_params.get('surname')
        if author_surname:
            queryset = queryset.filter(surname=author_surname)
        return queryset

    def get(self, request):
                return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
