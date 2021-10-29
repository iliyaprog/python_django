from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from app_news import models
from app_news.forms import NewsForm, AuthForm, AuthCommentForm, NewsCommentForm
from django.views import View
from django.views import generic
from app_news.models import News, Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля')
    else:
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из своей учетной записи')


class NewsFormView(generic.ListView):
    model = News
    template_name = 'title_news.html'
    context_object_name = 'all_news_list'
    queryset = News.objects.all()


class DetailNewsView(View):

    def get(self, request, profile_id):
        all_comments = list()
        news_model = News.objects.get(id=profile_id)
        comments = Comment.objects.all()
        for i_comment in comments:
            try:
                if i_comment.news.id == profile_id:
                    all_comments.append(i_comment)
            except:
                pass

        if all_comments == list():
            all_comments = None


        comment_form = AuthCommentForm()


        return render(request, 'detail_news.html', context={
            'profile_id': profile_id, 'news_model': news_model,
            'comment_form': comment_form, 'all_comments': all_comments})


    def post(self, request, profile_id):
        all_comments = list()
        news_model = News.objects.get(id=profile_id)
        comment_model = Comment()
        comment_form = NewsCommentForm(request.POST, instance=comment_model)

        if comment_form.is_valid():
            comment_model.save()

        comment_model.news = news_model
        comment_model.save()
        if request.user.is_authenticated:
            comment_model.author = request.user.first_name
            comment_model.save()
        else:
            comment_model.author = 'Аноним'
            comment_model.save()
        comments = Comment.objects.all()
        for i_comment in comments:
            try:
                if i_comment.news.id == profile_id:
                    all_comments.append(i_comment)
            except:
                pass
        if all_comments == list():
            all_comments = None
        comment_form = AuthCommentForm()

        return render(request, 'detail_news.html', context={
            'comment_form': comment_form, 'profile_id': profile_id,
            'news_model': news_model, 'all_comments': all_comments})


class CreateNewsView(View):

    def get(self, request):
        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied()
        news_form = NewsForm
        return render(request, 'create_news.html', context={'news_form': news_form})

    def post(self, request):
        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'create_news.html', context={'news_form': news_form})


class UpgreateNewsView(View):

    def get(self, request, profile_id):
        if not request.user.has_perm('app_news.change_news'):
            raise PermissionDenied
        news_model = News.objects.get(id=profile_id)
        news_form = NewsForm(instance=news_model)
        return render(request, 'upgreate_news.html', context={
            'profile_id': profile_id, 'news_form': news_form})

    def post(self, request, profile_id):
        if not request.user.has_perm('app_news.change_news'):
            raise PermissionDenied
        news_model = News.objects.get(id=profile_id)
        news_form = NewsForm(request.POST, instance=news_model)

        if news_form.is_valid():
            news_model.save()
        return render(request, 'upgreate_news.html', context={
            'profile_id': profile_id, 'news_form': news_form})

