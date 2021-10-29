from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from app_users.models import ProfileModel
from app_users.forms import ExtendedRegisterForm


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            num_phone = form.cleaned_data.get('num_phone')
            city = form.cleaned_data.get('city')
            data_of_birth = form.cleaned_data.get('data_of_birth')
            ProfileModel.objects.create(
                user=user,
                city=city,
                num_phone=num_phone,
                data_of_birth=data_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'registration.html', {'form': form})
