from rest_framework.pagination import PageNumberPagination


class BookResultsSetPagination(PageNumberPagination):
    page_size = 6
