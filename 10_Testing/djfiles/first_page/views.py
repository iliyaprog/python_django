from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import View

from app_users.forms import AuthForm
from app_media.models import Feed, FeedFile
from app_media.forms import UploadFileForm


class RecordsFormView(generic.ListView):
    model = Feed
    template_name = 'first_page.html'
    context_object_name = 'total_list'
    queryset = Feed.objects.all().order_by('-id')


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
                    return render(request, 'first_page.html', {})
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

class AnotherLogoutView(LogoutView):
    next_page = '/'


def get_detail_record(request, object_id):
    photo_list = list()
    record_model = Feed.objects.get(id=object_id)
    all_photo = FeedFile.objects.all()
    for i_photo in all_photo:
        try:
            if i_photo.feed.id == record_model.id:
                photo_list.append(i_photo)
        except:
            pass

    if photo_list == list():
        photo_list = None

    return render(request, 'detail_record.html', context={
        'photo_list': photo_list, 'record_model': record_model})
