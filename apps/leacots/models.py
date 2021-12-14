from django.db import models

# Create your models here.
class Leacots(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="ID", help_text="ID")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", auto_created=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    name = models.CharField(verbose_name="名称", help_text="名称", max_length=100)
    content = models.TextField(verbose_name="内容", help_text="内容")

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = 'tb_leacots'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id) + ":" + self.name

