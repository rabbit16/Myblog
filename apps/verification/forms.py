from django import forms
from django.db.models import Q
from apps.index.models import User
from django_redis import get_redis_connection

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=5, error_messages={
        "min_length": "最小长度是5位",
        "max_length": "最大长度是20位",
        "required": "用户名不能为空"
    })
    password = forms.CharField(max_length=20, min_length=5, error_messages={
        "min_length": "最小长度是5位",
        "max_length": "最大长度是20位",
        "required": "密码不能为空"
    })
    password_repeat = forms.CharField(max_length=20, min_length=5, error_messages={
        "min_length": "最小长度是5位",
        "max_length": "最大长度是20位",
        "required": "密码不能为空"
    })
    mobile = forms.CharField(max_length=11, min_length=11, error_messages={
        "min_length": "最小长度是1位",
        "max_length": "最大长度是11位",
        "required": "手机号不能为空"
    })
    picCode = forms.CharField(max_length=50, min_length=4, error_messages={
        "min_length": "最小长度是4位",
        "max_length": "最大长度是4位",
        "required": "图形验证码不能为空"
    })
    picNum = forms.CharField(max_length=4, min_length=4, error_messages={
        "min_length": "最小长度是4位",
        "max_length": "最大长度是4位",
        "required": "图形验证码不能为空"
    })


    def clean_username_mobile(self):
        username = self.cleaned_data.get('username')
        mobile = self.cleaned_data.get('mobile')
        if User.objects.filter(Q(username=username) | Q(mobile=mobile)).exists():
            return forms.ValidationError("用户名和手机号已经被注册了，请重新输入")
        return username, mobile

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        redis_base = get_redis_connection('verify_codes')
        picNum = cleaned_data.get('picNum')
        picNumInRedis = redis_base.get('img_{}'.format(cleaned_data.get('picCode'))).decode('utf8')
        if password != password_repeat:
            return forms.ValidationError("两次密码不一致")
        if picNum != picNumInRedis:
            return forms.ValidationError("验证码输入不正确")

