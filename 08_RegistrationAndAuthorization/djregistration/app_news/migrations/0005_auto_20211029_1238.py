# Generated by Django 2.2 on 2021-10-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0004_auto_20211028_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='flag_activate',
            field=models.BooleanField(default=False),
        ),
    ]
