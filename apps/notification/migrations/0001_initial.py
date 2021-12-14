# Generated by Django 3.2.8 on 2021-12-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('N_id', models.IntegerField(auto_created=True, help_text='ID', primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标题', max_length=100, verbose_name='标题')),
                ('content', models.TextField(help_text='内容', verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'db_table': 'tb_notification',
                'ordering': ['-update_time', '-N_id'],
            },
        ),
    ]
