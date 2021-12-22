from django.urls import path
from app_media.views import upload_file, model_form_upload, upload_files, upload_records

urlpatterns = [
    path('upload_file', upload_file, name='upload_file'),
    path('model_form_upload', model_form_upload, name='model_form_upload'),
    path('upload_files', upload_files, name='upload_files'),
    path('upload_records', upload_records, name='upload_records')
]