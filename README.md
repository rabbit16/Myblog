# 网站设计文档
## 环境介绍
python3.6的环境
MAC下开发

## 需求介绍

本网站属于小站，所以功能没有那么强大，主要就几个功能：

1. 博客功能
   1. 文章的发布
   2. 文章的更改
   3. 文章的查看
2. 资源下载功能
   1. Windows上的好东西
   2. MAC上的好东西
3. 电影播放功能(以后可以直播，或者放我的录播)
4. 后台管理
   1. 多少篇文章
   2. 删除文章
   3. 修改文章
   4. 增加文章

## 博客功能

### 页面设计和要求

#### 要求

需要做到页面简洁，不要花里胡哨

主题一定要明确，每个页面的风格和要求必须突出

#### 设计

##### 文章列表展示

##### 广告位预留

##### 评论位预留

##### 具体文章页

预留点赞的按钮

预留广告位

预留评论位

##### 留言页面

仿QQ的留言界面形式，仿造一个。

页面选取

页面样式更改

### 资源下载功能

## 表单设计

### 博客表单

#### 文章表单

##### 三表关系

有三个表，一个是文章表，一个是标签表，还有一个是它们之间的关联表。

由于文章和标签之间是多对多的关系，在Django中，我用manytomany字段，在Tag这个表里面设置了manytomany字段，同时through参数指定了第三章管理它们关系的表。

##### 字段设计

######  文章Article

```python
class Article(ModelBase):
    id = models.IntegerField(verbose_name='文章ID', help_text="文章ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name='文章标题',help_text='文章标题',max_length=150)
    content = MDTextField(verbose_name='文章内容',help_text='文章标题')
    abstract = models.TextField(verbose_name='摘要',help_text='文章标签',default=None)
    click = models.IntegerField(verbose_name='点击量',help_text='点击量',default=0)
    like_num = models.IntegerField(verbose_name='点赞数',help_text='点赞数',default=0)
    author_name = models.CharField(verbose_name="作者名字", help_text='作者名字', default='兔子', max_length=10)
    source = models.TextField(verbose_name="网址", help_text="网址", max_length=400, default='')
    update_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", default=timezone.now())
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    # tag = models.ForeignKey('Tag',on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering=['-update_time','-id']
        db_table = 'tb_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
```

###### Tag表单

```python
class Tag(models.Model):
    tag_name = models.CharField(verbose_name='标签',help_text='输入标签',max_length=64)
    tag_id = models.IntegerField(verbose_name='标签ID', help_text="标签ID", primary_key=True, auto_created=True)
    a_id = models.ManyToManyField('Article', through='AuthorAndTag')
    class Meta:
        verbose_name = '标签'
        db_table = 'tb_tag'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name
```

###### 关联表

```python
class AuthorAndTag(models.Model):
    article_id = models.ForeignKey('Article', on_delete=models.CASCADE)  # 外键关联
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)
    push_time = models.DateTimeField(verbose_name='时间', help_text="创建时间", auto_created=True, default=timezone.now())
    is_delete = models.BooleanField(verbose_name="软删除", help_text="软删除", default=0)
    class Meta:
        verbose_name = '书和标签'
        db_table = 'tb_tab_article'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ','.join([str(self.article_id), str(self.tag_id)])
```



##### 终端查看关系

先在终端运行：

`python manage.py makemigrations`

`python manage.py migrate`

然后我们在数据库中添加相应的内容

用Django自带的终端查看对应的表关系：

用反向查询，也就是直接查询第三章管理表

```bash
>>> AuthorAndTag.objects.all()[0]
<AuthorAndTag: AuthorAndTag object (1)>
>>> AuthorAndTag.objects.all()[0].article_id
<Article: 测试文章>
>>> AuthorAndTag.objects.all()[0].article_id.content
'测试内容如下'
>>> AuthorAndTag.objects.all()[0].tag_id.tag_name
'测试'
>>> AuthorAndTag.objects.all()[0].article_id.id
1

```

我们发现，article_id对应的就是我们具体的文章句柄。

同理，tag_id对应的就是我们的Tag句柄。

### 资源展示视图的表单设计

资源展示的表单我们仿造博客中，文章和标签的关系。

我们需要建立资源和标签的联系，从而在后期展示的时候可以按照标签的种类进行分类展示。