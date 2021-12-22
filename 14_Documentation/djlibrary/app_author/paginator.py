from rest_framework.pagination import PageNumberPagination


class AuthorResultsSetPagination(PageNumberPagination):
    """Класс пагинатор для настройки отображения API авторов"""
    page_size = 5
