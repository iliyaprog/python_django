from django.urls import path

from app_users.views import restore_password, login_view, another_register_view,\
    logout_view, update_user_account, user_account

urlpatterns = [
    path('restore_password/', restore_password, name='restore_password'),
    path('login/', login_view, name='login'),
    path('registration', another_register_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('update_user_account/', update_user_account, name='update_user_account'),
    path('user_account/', user_account, name='user_account'),
]
