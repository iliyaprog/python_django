from django.shortcuts import render
from app_score.models import Shop

def all_score(request):
    scores = Shop.objects.all()
    return render(request, 'all_score.html', context={'scores': scores})
