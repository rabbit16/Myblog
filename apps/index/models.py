from django.db import models
# from utils import ModelBase
from django.contrib.auth.models import UserManager as _UserManager,AbstractUser
# Create your models here.



class UserManager(_UserManager):
    def create_superuser(self, username, password, email=None, **extra_fields):
        super().create_superuser(username=username,email=email,password=password,**extra_fields)


class User(AbstractUser):
    objects = UserManager()
    REQUIRED_FIELDS = ['mobile']
    mobile = models.CharField(max_length=11,verbose_name='手机号',help_text="手机号",unique=True,
                               error_messages={'unique':"改手机号已注册"})
    email_ac =models.BooleanField(default=False,verbose_name="邮箱状态")
    class Meta:
        db_table ='tb_users'
        verbose_name = '用户'

    def __str__(self):
        return self.username