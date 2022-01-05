import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import logging

from utils.res_code import to_json_data, Code, error_map
from verification.forms import RegisterForm
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
                User.objects.create_user(username=registerForm.cleaned_data.get('username'),
                                         password=registerForm.cleaned_data.get('password'),
                                         mobile=registerForm.cleaned_data.get('mobile')
                                        )
            data = {
                'errno': Code.OK
            }
            return to_json_data(data=data)
        except:
            return to_json_data(errno=Code.NODATA, errmsg=error_map[Code.PICERROR])



