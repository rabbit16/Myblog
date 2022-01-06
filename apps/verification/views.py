from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from apps.index.models import User
from utils.captcha.captcha import captcha
from django_redis import get_redis_connection
import logging
from utils.res_code import to_json_data
# Create your views here.
logger = logging.getLogger('django')

class ImageCode(View):

    def get(self, request, img_codes):
        code, image = captcha.generate_captcha()
        con_redis = get_redis_connection('verify_codes')
        redis_key = 'img_{}'.format(img_codes)
        con_redis.setex(redis_key, 60, code)
        logger.info("IMAGE_CODE {}".format(code))
        return HttpResponse(content=image, content_type="image/jpg")

class UserNameCheck(View):

    def get(self, request, username):
        data = {
            "username": username,
            'count': User.objects.filter(username=username).count()
        }
        return to_json_data(data=data)

class MobileCheck(View):
    def get(self, request, mobile):
        data = {
            'mobile': mobile,
            'count': User.objects.filter(mobile=mobile).count()
        }
        return to_json_data(data=data)



