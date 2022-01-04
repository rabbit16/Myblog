from django.shortcuts import render
from django.views import View
import logging
from utils.captcha.captcha import captcha

# Create your views here.
logger = logging.getLogger('django')
class Index(View):
    def get(self,request):
        return render(request, 'index/index.html')

class Register(View):
    def get(self, request):
        code, image = captcha.generate_captcha()
        return render(request, 'index/register.html')
# class Intro(View):
#     def get(self,request):
#         pic_t = ContextImage.objects.only('id','name','text','img_url').filter(is_delete=False)
#         return render(request, 'dco/index.html',context={
#             'pic_t':pic_t
#         })
#
