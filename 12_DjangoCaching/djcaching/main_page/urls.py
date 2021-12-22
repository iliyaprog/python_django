from django.urls import path

from main_page.views import first_page

urlpatterns = [
    path('', first_page, name='first_page'),
]