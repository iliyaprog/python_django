from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import render, redirect
from app_users.forms import ExtendedRegisterForm, EditForm
from app_users.models import ProfileModel
from django.contrib.auth.models import Group


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
            return redirect('/')
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