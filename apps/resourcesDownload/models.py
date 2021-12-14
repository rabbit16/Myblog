from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from utils.ModelBases import ModelBase
from mdeditor.fields import MDTextField
# Create your tests here.

class Resource(ModelBase):
    id = models.IntegerField(verbose_name='资源ID', help_text="资源ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name='资源标题', help_text='资源标题', max_length=150)
    abstract = models.TextField(verbose_name='摘要', help_text='资源标签', default=None)
    click = models.IntegerField(verbose_name='点击量', help_text='点击量', default=0)
    like_num = models.IntegerField(verbose_name='点赞数', help_text='点赞数', default=0)
    source = models.TextField(verbose_name="网址", help_text="网址", max_length=400, default='')
    update_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", default=timezone.now())
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    img_url = models.CharField(verbose_name='图片路径', help_text='图片路径', default="../../media/img/lgd.png", max_length=100)
    downloadUrl = models.CharField(verbose_name="下载路径", help_text="下载路径", max_length=1000)
    # tag = models.ForeignKey('Tag',on_delete=models.SET_NULL,null=True)
    tags = TaggableManager(blank=True)
    type = models.CharField(verbose_name="文件类型", help_text="文件类型", max_length=100, default='')
    class Meta:
        ordering = ['-update_time', '-id']
        db_table = 'tb_resource'
        verbose_name = '资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(verbose_name='标签', help_text='输入标签',max_length=64)
    tag_id = models.IntegerField(verbose_name='标签ID', help_text="标签ID", primary_key=True, auto_created=True)
    r_id = models.ManyToManyField('Resource')
    img_url = models.CharField(verbose_name='图片路径', help_text='图片路径', default="../../media/img/lgd.png", max_length=100)
    class Meta:
        verbose_name = '标签'
        db_table = 'tb_resource_tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

class ResourceAndTag(models.Model):
    resource_id = models.ForeignKey('Resource', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)
    push_time = models.DateTimeField(verbose_name='时间', help_text="创建时间", auto_created=True, default=timezone.now())
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    class Meta:
        verbose_name = '资源和标签'
        db_table = 'tb_tag_manage_resource'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ','.join([str(self.resource_id), str(self.tag_id)])