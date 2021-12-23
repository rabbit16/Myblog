import datetime

from django.utils import timezone
from haystack import indexes
from blog.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    author = indexes.CharField(model_attr='author_name')  # 创建一个author字段
    title = indexes.CharField(model_attr='title')
    abstract = indexes.CharField(model_attr='abstract')
    create_time = indexes.DateTimeField(model_attr='create_time')  # 创建一个create_time字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return Article  # 传入文章对象

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(is_delete=False)