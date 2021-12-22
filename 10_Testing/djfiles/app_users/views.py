from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from app_users.forms import ExtendedRegisterForm, EditForm, RestorePassword
from app_users.models import ProfileModel
from django.contrib.auth.models import Group, User


def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            ProfileModel.objects.create(
                user=user,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            good_users = Group.objects.get(name='Верифицированные пользователи')
            user.groups.add(good_users)
            return redirect('first_page')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'app_users.html', {'form': form})


def edit_view(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            request.user.first_name = first_name
            request.user.save()
            request.user.last_name = last_name
            request.user.save()
            return redirect('/')
    else:
        form = EditForm()
    return render(request, 'edit_users.html', {'form': form})

def password_recovery(request):
    if request.method == 'POST':
        form = RestorePassword(request.POST)
        if form.is_valid():
            new_password = User.objects.make_random_password()
            user_email = form.cleaned_data['email']
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message='Test',
                from_email='admin@company.com',
                recipient_list=[form.cleaned_data['email']]
            )
            return HttpResponse('Письмо с новым паролем было отправлено на email')
    restore_password_form = RestorePassword()
    context = {'form': restore_password_form}
    return render(request, 'password_recovery.html', context=context)
