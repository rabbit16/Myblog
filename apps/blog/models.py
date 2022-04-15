from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from utils.ModelBases import ModelBase
from mdeditor.fields import MDTextField
# Create your models here.


class Article(ModelBase):
    id = models.AutoField(verbose_name='文章ID', help_text="文章ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name='文章标题', help_text='文章标题', max_length=150)
    # content = MDTextField(verbose_name='文章内容', help_text='文章内容')
    content = models.TextField(verbose_name='文章内容', help_text='文章内容', default='')
    abstract = models.TextField(verbose_name='摘要', help_text='文章标签', default=None)
    click = models.IntegerField(verbose_name='点击量', help_text='点击量', default=0)
    like_num = models.IntegerField(verbose_name='点赞数', help_text='点赞数', default=0)
    author_name = models.CharField(verbose_name="作者名字", help_text='作者名字', default='兔子', max_length=10)
    source = models.CharField(verbose_name="网址", help_text="网址", max_length=400, default='')
    update_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", default=timezone.now)
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    img_url = models.CharField(verbose_name='图片路径', help_text='图片路径', default="../../media/img/lgd.png", max_length=100)
    # tag = models.ManyToManyField('Tag', default="")
    tags = TaggableManager(blank=True)
    class Meta:
        ordering = ['-update_time', '-id']
        db_table = 'tb_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(verbose_name='标签', help_text='输入标签', max_length=64)
    tag_id = models.IntegerField(verbose_name='标签ID', help_text="标签ID", primary_key=True, auto_created=True)
    articles = models.ManyToManyField('Article', through='AuthorAndTag')
    # articles = models.ManyToManyField('Article')
    img_url = models.CharField(verbose_name='图片路径', help_text='图片路径', max_length=100)
    class Meta:
        verbose_name = '标签'
        db_table = 'tb_tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

class AuthorAndTag(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)
    push_time = models.DateTimeField(verbose_name='时间', help_text="创建时间", auto_created=True, default=timezone.now)
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    class Meta:
        verbose_name = '书和标签'
        db_table = 'tb_tag_article'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ','.join([str(self.article_id), str(self.tag_id)])

# class Comments(ModelBase):
#     content = models.TextField(verbose_name='评论',help_text='评论')
#     author = models.ForeignKey('index.User', on_delete=models.SET_NULL, null=True)
#     article = models.ForeignKey('blog.Article',on_delete=models.CASCADE)
#     parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
#
#     class Meta:
#         ordering = ['-update_time', '-id']
#         db_table = "tb_comment"  # 指明数据库表名
#         verbose_name = "评论"  # 在admin站点中显示的名称
#         verbose_name_plural = verbose_name  # 显示的复数名称
#
#     def to_dict_data(self):
#         comment_dict = {
#             'news_id': self.article.id,
#             'content_id': self.id,
#             'content': self.content,
#             'author': self.author.username,
#             'update_time': self.update_time.strftime('%Y年%m月%d日 %H:%M'),
#             'parent': self.parent.to_dict_data() if self.parent else None,#这个想法是一个递归，这个需要重点掌握。
#         }
#         return comment_dict







