# Generated by Django 3.2.8 on 2021-12-14 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesDownload', '0006_auto_20211213_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 14, 11, 25, 18, 434994), help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='resourceandtag',
            name='push_time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 12, 14, 11, 25, 18, 435857), help_text='创建时间', verbose_name='时间'),
        ),
    ]
