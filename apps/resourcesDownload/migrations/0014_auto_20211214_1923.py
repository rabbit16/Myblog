# Generated by Django 3.2.8 on 2021-12-14 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesDownload', '0013_auto_20211214_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 14, 19, 23, 4, 341991), help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='resourceandtag',
            name='push_time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 12, 14, 19, 23, 4, 342889), help_text='创建时间', verbose_name='时间'),
        ),
    ]
