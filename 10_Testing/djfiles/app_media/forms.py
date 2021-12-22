from django import forms
from django.forms import TextInput
from app_media.models import Feed, FeedFile


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=350)
    file = forms.ImageField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('text', )


class UploadForm(forms.Form):
    file = forms.FileField()


class MultiFileForm(forms.Form):
    file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


