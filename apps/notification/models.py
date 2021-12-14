from django.db import models
from utils import ModelBases


# Create your models here.

class Notification(models.Model):
    N_id = models.IntegerField(verbose_name="ID", help_text="ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name="标题", help_text="标题", max_length=100)
    content = models.TextField(verbose_name="内容", help_text="内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        ordering = ['-update_time', '-N_id']
        db_table = 'tb_notification'
        verbose_name = '公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
