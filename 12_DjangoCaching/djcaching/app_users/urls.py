from django.urls import path

from app_users.views import login_view, register_view, logout_view, user_page_view, upload_avatar_view, edit_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('user_page', user_page_view, name='user_page'),
    path('upload_avatar', upload_avatar_view, name='upload_avatar'),
    path('redactor_user', edit_view, name='redactor_user')
]