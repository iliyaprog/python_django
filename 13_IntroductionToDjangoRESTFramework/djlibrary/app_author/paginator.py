from rest_framework.pagination import PageNumberPagination


class AuthorResultsSetPagination(PageNumberPagination):
    page_size = 5
