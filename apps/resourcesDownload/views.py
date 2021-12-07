import math

from django.shortcuts import render
from django.views import View
from blog.models import *
import logging

# Create your views here.
class Resource(View):
    def get(self, request):
        # try:
        #     tag = Tag.objects.all()[(page_num-1)*8: page_num*8]
        # except:
        #     tag = Tag.objects.all()[(page_num-1)*8:]
        tag = Tag.objects.all()[:8]
        all_obj = Tag.objects.count()
        pag_num = math.ceil(Tag.objects.count()/8)
        now_page = 1
        tag_dict = {
            'tags': tag,
            'page_num': pag_num,
            'all_num': all_obj,
            'now_page': now_page
        }
        return render(request, 'resourcePage/listsource.html', context=tag_dict)

class ResourcePageShow(View):
    def get(self, request, page_num):
        all_obj = Tag.objects.count()
        page_all = math.ceil(Tag.objects.count() / 8)
        if page_num <= 0 or page_num > page_all:
            page_num = 1
        try:
            tag = Tag.objects.all()[(page_num-1)*8: page_num*8]
        except:
            tag = Tag.objects.all()[(page_num-1)*8:]
        tag_dict = {
            'tags': tag,
            'page_num': page_all,
            'all_num': all_obj,
            'now_page': page_num
        }
        return render(request, 'resourcePage/listsource.html', context=tag_dict)

# class ResourcePageJianShow(View):
#     def get(self, request, page_num=1):
#         try:
#             tag = Tag.objects.all()[(page_num-1)*8: page_num*8]
#         except:
#             tag = Tag.objects.all()[(page_num-1)*8:]
#         all_obj = Tag.objects.count()
#         pag_num = math.ceil(Tag.objects.count() / 8)
#         tag_dict = {
#             'tags': tag,
#             'page_num': pag_num-1,
#             'all_num': all_obj
#         }
#         return render(request, 'resourcePage/listsource.html', context=tag_dict)