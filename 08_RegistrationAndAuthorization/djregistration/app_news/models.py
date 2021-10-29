from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User



class News(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Заголовок')
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    tag = models.CharField(max_length=50, default='нет', verbose_name='Тэг')
    flag_activate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        permissions = (('can_publish', 'Может публиковать'),)

    def __str__(self):
        return f'{self.id}. {self.title} ({self.created_at}, {self.flag_activate})'


class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, default=None, null=True, verbose_name='User', blank=True)
    news = models.ForeignKey(
        'News', on_delete=models.CASCADE,
        default=None,
        verbose_name='Новость',
        null=True
    )
    author = models.CharField(max_length=100,
                              default=None,
                              verbose_name='Автор комментария',
                              null=True
                              )
    text = models.TextField(max_length=1000,
                            verbose_name='Текст комментария',
                            default=None,
                            null=True
                            )

    def __str__(self):
        return f'{self.author}: {self.text}'


class CommentNews(models.Model):
    title = models.CharField(max_length=30)
    comment = models.ManyToManyField(Comment)
    news = models.ForeignKey(News, on_delete=models.CASCADE)


