# Generated by Django 3.2.8 on 2021-12-14 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesDownload', '0009_auto_20211214_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 14, 11, 32, 12, 962020), help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='resourceandtag',
            name='push_time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 12, 14, 11, 32, 12, 962885), help_text='创建时间', verbose_name='时间'),
        ),
    ]
