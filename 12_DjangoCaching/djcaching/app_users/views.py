from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_users.forms import ExtendedRegisterForm, AuthForm, AvatarForms, EditForm
from django.utils.translation import gettext_lazy as _
from app_users.models import Avatar, Bonus, ShoppingList
from main_page.models import Product
from app_products.models import PromotionsAndOffers
from django.core.cache import cache



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
                    return redirect('/')
                else:
                    auth_form.add_error('__all__', _('Mistake! The user account is inactive.'))
            else:
                auth_form.add_error('__all__', _('Mistake! Check the spelling of the username and password.'))
    else:
        auth_form = AuthForm()

    context = {
        'form': auth_form
    }
    return render(request, 'login.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            good_users = Group.objects.get(name='Верифицированные пользователи')
            user.groups.add(good_users)
            Bonus.objects.create(user=user)
            ShoppingList.objects.create(user=user)

            return HttpResponse(_('Welcome'))
    else:
        form = ExtendedRegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse(_('You have logged out of your account'))

def user_page_view(request):
    avatar = None
    bonus = None
    profile = request.user
    avatars = Avatar.objects.all()
    for i_avatar in avatars:
        if i_avatar.user == request.user:
            avatar = i_avatar
            break
    bonus = Bonus.objects.get(user=request.user)
    shop_list = (ShoppingList.objects.get(user=request.user))
    shop_list = shop_list.shop_list.split(',')
    products = []
    for i in shop_list:
        try:
            products.append(Product.objects.get(id=int(i)))
        except:
            pass
    if products == []:
        products = None

    username = request.user.username
    offers_cache_key = 'promotions:{}'.format(username)
    offers = PromotionsAndOffers.objects.all()

    user_account_cache_data = {
        offers_cache_key: offers
    }

    cache.set_many(user_account_cache_data, 1800)

    return render(request, 'user_page.html', {'profile': profile, 'avatar': avatar, 'bonus': bonus,
                                              'products': products, 'offers': offers})



def upload_avatar_view(request):
    if request.method == 'POST':
        upload_file_form = AvatarForms(request.POST, request.FILES)
        if upload_file_form.is_valid():
            if Avatar.objects.get(user=request.user):
                Avatar.objects.get(user=request.user).delete()
            file = request.FILES['file']
            file_instance = Avatar(user=request.user, avatar=file)
            file_instance.save()
            return redirect('/app_users/user_page')
    else:
        upload_file_form = AvatarForms()

    context = {'form': upload_file_form}
    return render(request, 'upload_avatar.html', context=context)

def edit_view(request):
    if request.method == 'POST':
        form_edit = EditForm(request.POST)
        if form_edit.is_valid():
            first_name = form_edit.cleaned_data.get('first_name')
            last_name = form_edit.cleaned_data.get('last_name')
            email = form_edit.cleaned_data.get('email')
            request.user.first_name = first_name
            request.user.save()
            request.user.last_name = last_name
            request.user.save()
            request.user.email = email
            request.user.save()
            return redirect('/app_users/user_page')
    else:
        form_edit = EditForm()
    return render(request, 'edit_users.html', {'form_edit': form_edit})
