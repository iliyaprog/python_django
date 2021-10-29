from django import forms
from app_news.models import News, Comment
from django.forms import ModelForm


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'tag']


class NewsCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']


class AuthCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)