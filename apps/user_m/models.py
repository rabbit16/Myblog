
from django.contrib.auth.models import AbstractUser,UserManager as _UserManager
from django.db import models
# Create your models here.
class SuperUserManager(_UserManager):
    def create_superuser(self, username, password,email=None,**extra_fields):
        super().create_superuser(username=username, email=email,password=password, **extra_fields)#不需要传递self不然就会报错

class Users(AbstractUser):#先要注册替换用户的类，然后再迁移
    objects = SuperUserManager()#这个是让我们自定义的属性生效
    email_mc = models.BooleanField(default=False,verbose_name='邮箱状态')

    REQUIRED_FIELDS = ['mobile']
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', help_text='手机号',
                              error_messages={'unique': '此手机号已经注册'},default=None)
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'

    def __str__(self):
        return self.username


