from django.urls import path
from title_news.views import first_page


urlpatterns = [
    path('', first_page, name='first_page'),
]
