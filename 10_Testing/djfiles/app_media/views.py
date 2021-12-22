from _csv import reader
from decimal import Decimal

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_media.forms import DocumentForm, MultiFileForm, UploadForm, UploadFileForm
from app_media.models import FeedFile, Feed
import csv


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {'form': upload_file_form}
    return render(request, 'upload_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'file_form_upload.html', {'form': form})


def upload_files(request):
    if not request.user.has_perm('app_media.add_feed'):
        raise PermissionDenied()
    if request.method == 'POST':
        upload_form = MultiFileForm(request.POST, request.FILES)
        another_form = DocumentForm(request.POST)
        if upload_form.is_valid() and another_form.is_valid():
            text = another_form.cleaned_data.get('text')
            instance = Feed(text=text, user=request.user)
            instance.save()
            files = request.FILES.getlist('file_field')
            for i in files:
                file_instance = FeedFile(file=i, feed=instance)
                file_instance.save()
            return redirect('/')
    else:
        upload_form = MultiFileForm()
        another_form = DocumentForm()
    return render(request, 'upload_files.html', {'upload_form': upload_form, 'another_form': another_form})


def upload_records(request):

    if not request.user.has_perm('app_media.add_feed'):
        raise PermissionDenied()
    if request.method == 'POST':
        upload_file_form = UploadForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            records_file = upload_file_form.cleaned_data['file'].read()
            records_str = records_file.decode('utf-8').split('\n')
            csv_reader = csv.reader(records_str, delimiter=';', quotechar='"')
            for row in csv_reader:
                try:
                    new_object = Feed.objects.create(user=request.user, text=row[1])
                    new_object.save()
                    all_photo = row[2].split(',')
                    for i_photo in all_photo:
                        photo_object = FeedFile.objects.create(file=i_photo, feed=new_object)
                        photo_object.save()
                except:
                    pass
            return HttpResponse(content='Записи успешно обновлены', status=200)
    else:
        upload_file_form = UploadForm()

    context = {'form': upload_file_form}
    return render(request, 'download_records.html', context=context)

