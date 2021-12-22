from rest_framework.pagination import PageNumberPagination


class BookResultsSetPagination(PageNumberPagination):
    """Класс пагинатор для настройки отображения API книг"""
    page_size = 6
