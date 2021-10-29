from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from app_news import models
from app_news.forms import NewsForm, NewsCommentForm, AuthForm, AuthCommentForm
from django.views import View
from django.views import generic
from app_news.models import News, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView


def first_page(request):
    return render(request, 'first_page.html', {})

