from django.urls import path

from app_score.views import all_score

urlpatterns = [
    path('all_score/', all_score, name='all_score'),
    ]