# Generated by Django 3.2.8 on 2021-12-15 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesDownload', '0016_auto_20211215_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 10, 57, 34, 326719), help_text='创建时间', verbose_name='创建时间'),
        ),
    ]
