from django.urls import path
from first_page.views import login_view, AnotherLogoutView, RecordsFormView, get_detail_record

urlpatterns = [
    path('', RecordsFormView.as_view(), name='first_page'),
    path('login/', login_view, name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('detail_record/<int:object_id>', get_detail_record, name='detail_record')
]