import json

from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
import logging

from utils.res_code import to_json_data, Code, error_map
from verification.forms import RegisterForm, LoginForm
from apps.index.models import User

# Create your views here.
logger = logging.getLogger('django')

class Index(View):
    def get(self, request):
        return render(request, 'index/index.html')

class Register(View):
    def get(self, request):
        return render(request, 'index/register.html')

    def post(self, request):
        params = json.loads(request.body)
        registerForm = RegisterForm(params)
        try:
            if registerForm.is_valid():
                user = User.objects.create_user(username=registerForm.cleaned_data.get('username'),
                                         password=registerForm.cleaned_data.get('password'),
                                         mobile=registerForm.cleaned_data.get('mobile')
                                        )
                login(request, user)
            data = {
                'errno': Code.OK
            }
            return to_json_data(data=data)
        except:
            return to_json_data(errno=Code.NODATA, errmsg=error_map[Code.PICERROR])


class Login(View):
    def get(self, request):
        return render(request, 'index/login.html')

    def post(self, request):
        json_data = json.loads(request.body)
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg='参数错误')

        else:
            loginForm = LoginForm(data=json_data, request=request)
            try:
                if loginForm.is_valid():
                    return to_json_data(errmsg="登录成功")
                else:
                    err_m_l = []
                    for i in loginForm.errors.values():
                        err_m_l.append(i[0])
                    err_msg_str = '/'.join(err_m_l)
                    return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)
            except:
                return to_json_data(errno=Code.PARAMERR, errmsg='参数错误')

class LoginOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index:login"))
