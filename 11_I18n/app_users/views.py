from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from app_users.forms import AuthForm, RegisterForm, UserForm, RestorePasswordForm, UploadFileForm


# from app_users.models import Profile
# from module_9.django_example_source.app_users.forms import UploadFileForm
from app_users.models import User


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


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
                    return redirect('/app_goods/items')
                else:
                    auth_form.add_error('__all__', _('Mistake! The user account is inactive.'))
            else:
                auth_form.add_error('__all__', _('Mistake! Check the spelling of the username and password.'))
    else:
        auth_form = AuthForm()

    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponse(_('You have successfully logged out from under your account'))


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.refresh_from_db()

            user.city = form.cleaned_data.get('city')
            user.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.email = form.cleaned_data.get('email')
            user.city = form.cleaned_data.get('city')
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# def upload_file(request):
#     if request.method == 'POST':
#         upload_file_form = UploadFileForm(request.POST, request.FILES)
#         if upload_file_form.is_valid():
#             uploaded_file = request.FILES['file']
#
#             return HttpResponse(content= uploaded_file, status=200)
#     else:
#         upload_file_form = UploadFileForm()
#
#     context = {
#         'form': upload_file_form
#     }
#     return render(request, 'users/upload_file.html', context=context)


def user_account(request):
    return render(request, 'users/account.html')


def update_user_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()

            return redirect('/app_users/user_account')
    else:
        user_form = UserForm()

    context = {
        'form': user_form
    }
    return render(request, 'users/edit_account.html', context=context)


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
                send_mail(subject=_('Password recovery'),
                          message=_(f'New password: {new_password}'),
                          from_email='admin@company.com',
                          recipient_list=[form.cleaned_data['email']])
                return HttpResponse(_('An email with a new password has been successfully sent'))

    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
