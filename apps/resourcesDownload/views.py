import json
import math
import logging
import os.path
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from resourcesDownload.models import *
from django.http import FileResponse, HttpResponse, JsonResponse, StreamingHttpResponse
from django.core.paginator import Paginator

logger = logging.getLogger('django')
# Create your views here.
page_show_every_page = 4
class ResourceShow(View):

    def get(self, request):
        tag = Tag.objects.all()[:page_show_every_page]
        all_obj = Tag.objects.count()
        pag_num = math.ceil(Tag.objects.count()/page_show_every_page)
        if pag_num == 0:
            pag_num = 1
        now_page = 1
        tag_dict = {
            'tags': tag,
            'page_num': pag_num,
            'all_num': all_obj,
            'now_page': now_page
        }
        return render(request, 'resourcePage/listsourceTag.html', context=tag_dict)

class ResourcePageShow(View):
    def get(self, request, page_num):
        all_obj = Tag.objects.count()
        page_all = math.ceil(Tag.objects.count() / page_show_every_page)
        if page_all == 0:
            page_all = 1
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
        return render(request, 'resourcePage/listsourceTag.html', context=tag_dict)

class SpecificResource(View):

    def get(self, request, tag_name):
        resource = Resource.objects.filter(tags__name__in=[tag_name])
        page_obj_all = Paginator(resource, page_show_every_page)
        page_go = 0
        if request.GET.get('page_to'):
            page_go = int(request.GET.get('page_to'))
        if request.GET.get('page_up'):
            page_go = int(request.GET.get('page_up')) + 1
        elif request.GET.get('page_down'):
            page_go = int(request.GET.get('page_down')) - 1
        if page_go == 0:
            now_page = 1
            resource_dict = {
                "now_page": now_page,
                'resources': page_obj_all.get_page(now_page),
                "page_num": page_obj_all.num_pages,
                "all_num": resource.count(),
                "page_every_show": page_show_every_page,
                "tag_name": tag_name

            }
            return render(request, 'resourcePage/listsource.html', context=resource_dict)
        else:
            if page_go > page_obj_all.num_pages:
                page_go = page_obj_all.num_pages
            if page_go < 1:
                page_go = 1
            resource_dict = {
                "now_page": page_go,
                'resources': page_obj_all.get_page(page_go),
                "page_num": page_obj_all.num_pages,
                "all_num": resource.count(),
                "page_every_show": page_show_every_page,
                "tag_name": tag_name
            }
            return render(request, 'resourcePage/listsource.html', context=resource_dict)

class FileDownload(View):

    @csrf_exempt
    def get(self, request):
        data_id = request.GET.get("source_id")
        file = Resource.objects.filter(id=data_id)[0].title
        file_path = "media/download/{}".format(file)
        # downloadFile = open(file_path, 'rb')
        if not os.path.isfile("media/download/{}".format(file)):  # 判断下载文件是否存在
            return HttpResponse("Sorry but Not Found the File")

        def file_iterator(chunk_size=1024):
            """
            文件生成器,防止文件过大，导致内存溢出
            :param file_p: 文件绝对路径
            :param chunk_size: 块大小
            :return: 生成器
            """
            try:
                with open(file_path, mode='rb') as f:
                    while True:
                        c = f.read(chunk_size)
                        if c:
                            yield c
                        else:
                            break
            except:
                return HttpResponse("该文件不存在哦～")
        # response = FileResponse(downloadFile)
        response = StreamingHttpResponse(file_iterator())
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(os.path.basename(file))
        return response