# Generated by Django 3.2.8 on 2021-12-13 11:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.IntegerField(auto_created=True, help_text='资源ID', primary_key=True, serialize=False, verbose_name='资源ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('title', models.CharField(help_text='资源标题', max_length=150, verbose_name='资源标题')),
                ('abstract', models.TextField(default=None, help_text='资源标签', verbose_name='摘要')),
                ('click', models.IntegerField(default=0, help_text='点击量', verbose_name='点击量')),
                ('like_num', models.IntegerField(default=0, help_text='点赞数', verbose_name='点赞数')),
                ('source', models.TextField(default='', help_text='网址', max_length=400, verbose_name='网址')),
                ('update_time', models.DateTimeField(default=datetime.datetime(2021, 12, 13, 11, 32, 13, 245383), help_text='创建时间', verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=0, help_text='软删除', verbose_name='软删除')),
                ('img_url', models.CharField(default='../../media/img/lgd.png', help_text='图片路径', max_length=100, verbose_name='图片路径')),
                ('downloadUrl', models.CharField(help_text='下载路径', max_length=1000, verbose_name='下载路径')),
                ('type', models.CharField(default='', help_text='文件类型', max_length=100, verbose_name='文件类型')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': '资源',
                'verbose_name_plural': '资源',
                'db_table': 'tb_resource',
                'ordering': ['-update_time', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.IntegerField(auto_created=True, help_text='标签ID', primary_key=True, serialize=False, verbose_name='标签ID')),
                ('tag_name', models.CharField(help_text='输入标签', max_length=64, verbose_name='标签')),
                ('img_url', models.CharField(default='../../media/img/lgd.png', help_text='图片路径', max_length=100, verbose_name='图片路径')),
                ('r_id', models.ManyToManyField(to='resourcesDownload.Resource')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tb_resource_tag',
            },
        ),
        migrations.CreateModel(
            name='ResourceAndTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_time', models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 12, 13, 11, 32, 13, 246240), help_text='创建时间', verbose_name='时间')),
                ('is_delete', models.BooleanField(default=0, help_text='软删除', verbose_name='软删除')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesDownload.resource')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesDownload.tag')),
            ],
            options={
                'verbose_name': '资源和标签',
                'verbose_name_plural': '资源和标签',
                'db_table': 'tb_tag_manage_resource',
            },
        ),
    ]
