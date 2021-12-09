import math

from django.shortcuts import render
from django.views import View
from resourcesDownload.models import *

# Create your views here.
page_show_every_page = 4
class Resource(View):

    def get(self, request):
        tag = Tag.objects.all()[:page_show_every_page]
        all_obj = Tag.objects.count()
        pag_num = math.ceil(Tag.objects.count()/page_show_every_page)
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
        page_all = math.ceil(Tag.objects.count() / page_show_every_page)
        if page_num <= 0 or page_num > page_all:
            page_num = 1
        try:
            tag = Tag.objects.all()[(page_num-1)*page_show_every_page: page_num*page_show_every_page]
        except:
            tag = Tag.objects.all()[(page_num-1)*page_show_every_page:]
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
#             tag = Tag.objects.all()[(page_num-1)*page_show_every_page: page_num*page_show_every_page]
#         except:
#             tag = Tag.objects.all()[(page_num-1)*page_show_every_page:]
#         all_obj = Tag.objects.count()
#         pag_num = math.ceil(Tag.objects.count() / page_show_every_page)
#         tag_dict = {
#             'tags': tag,
#             'page_num': pag_num-1,
#             'all_num': all_obj
#         }
#         return render(request, 'resourcePage/listsource.html', context=tag_dict)