import json
import math
import logging
import os

from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from haystack.views import SearchView
from markdown.extensions.toc import TocExtension, slugify
from utils.yolov5.detect import parse_opt, main
from blog import models
import markdown
import sys
# sys.path.insert(0, '../yolo')
from base64 import b64decode

# Create your views here.
page_show_num = 3
tag_show_num = 8

logger = logging.getLogger('django')
class ContextShow(View):
    def get(self, request):
        articles = models.Article.objects.filter(is_delete=0)
        try:
            articles = articles[0:page_show_num]  # 首页就展示前page_show_num个文章
        except:
            articles = articles[0:]
        return render(request, 'message/article_first.html', context={
            'articles': articles
        })

class ArticleContentShow(View):
    def get(self, request, a_id):
        news = models.Article.objects.get(id=a_id)
        news.click += 1
        news.save()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            'markdown.extensions.toc',  # 自动生成目录
            'sane_lists',
            TocExtension(slugify=slugify),
            'tables'
        ])
        # news.content = markdown.markdown(news.content, extensions=[
        #     'markdown.extensions.extra',
        #     'markdown.extensions.codehilite',  # 语法高亮拓展
        #     'markdown.extensions.toc',  # 自动生成目录
        #     'sane_lists',
        #     TocExtension(slugify=slugify),
        #     'tables'
        # ])  # 修改blog.content内容为html
        news.content = md.convert(news.content)
        return render(request, 'message/article_detail.html', context={
            'article': news,
            'toc': md.toc
        })

class ArticleListByTag(View):
    def get(self, request):
        now_page = 1
        try:
            next_page = int(request.GET.get("page_num"))
        except:
            next_page = 1
        if next_page:
            now_page = next_page
        tag = models.Tag.objects.all()
        all_show_project = Paginator(tag, tag_show_num)
        all_obj = models.Tag.objects.count()
        pag_num = all_show_project.num_pages
        if now_page > pag_num:
            now_page = pag_num
        if now_page < 1:
            now_page = 1

        tag_dict = {
            'tags': all_show_project.get_page(now_page),
            'page_num': pag_num,
            'all_num': all_obj,
            'now_page': now_page,
            "page_every_show": page_show_num
        }
        return render(request, 'message/article_tag_list.html', context=tag_dict)


class ArticleListDetailByTag(View):
    @csrf_exempt
    def get(self, request, tag_id):
        # tag_name = models.Tag.objects.filter(tag_id=tag_id)[0].tag_name  # 根据标签id获取标签名
        # tag_name = [i for i in jieba.cut(tag_name, cut_all=True)][-1]

        articles = models.Tag.objects.filter(tag_id=tag_id)[0].articles.filter(is_delete=0)[:page_show_num]
        # articles = models.Article.objects.filter(tags__name__in=[tag_name], is_delete=0)[:page_show_num]  # 从文章中匹配对应的标签文章
        # articles_count = models.Article.objects.filter(tags__name__in=[tag_name]).count()  # 数量
        articles_count = models.Tag.objects.filter(tag_id=tag_id)[0].articles.count()  # 数量
        page_num = math.ceil(articles_count/page_show_num)  #
        # page_now = 1
        # page_tag_list = [page_now, tag_id]
        final_page = [page_num, tag_id]
        first_page = [1, tag_id]
        articles_dict = {
            'articles': articles,
            'page_num': page_num,
            # 'page_now': page_now,
            'all_num': articles_count,
            'tag_id': tag_id,
            # 'page_tag_list': page_tag_list,
            'final_page': final_page,
            'first_page': first_page,
            'every_page_show': page_show_num
        }
        return render(request, 'message/article_list.html', context=articles_dict)

    @csrf_exempt
    def post(self, request, tag_id):
        final_page_flag = 0
        to_page_flag = 0
        tag_name = models.Tag.objects.filter(tag_id=tag_id)[0].tag_name
        # tag_name = [i for i in jieba.cut(tag_name, cut_all=True)][-1]
        all_num = models.Article.objects.filter(tag__tag_name=tag_name, is_delete=0).count()
        page_all = math.ceil(all_num / page_show_num)
        page_num = json.loads(request.body)
        page_num = int(page_num['page_num']) + 1
        try:
            final_page_flag = json.loads(request.body)['final']
        except:
            pass
        try:
            to_page_flag = json.loads(request.body)['toPage']
        except:
            pass
        if to_page_flag:
            page_num = to_page_flag

        if (page_num <= 0 or page_num > page_all) and final_page_flag != 1:
            page_num = 1
        if final_page_flag:
            page_num = page_all
        try:
            articles = models.Article.objects.filter(tag__tag_name=tag_name, is_delete=0)[(page_num - 1) * page_show_num: page_num * page_show_num]
        except:
            articles = models.Article.objects.filter(tag__tag_name=tag_name, is_delete=0)[(page_num - 1) * page_show_num:]
        articles = self.convert_to_dicts(articles)
        # json_data = serializers.serialize("json", MyModel.objects.all())
        articles_dict = {
            'articles': articles,
            'page_num': page_all,
            'all_num': all_num,
            'page_now': page_num,
            'tag_id': tag_id,
            'page_tag_list': 1,
            'every_page_show': page_show_num
        }
        # return render(request, 'message/article_list.html', context=articles_dict)
        return JsonResponse(articles_dict)

    def convert_to_dicts(self, objs):
        '''把对象列表转换为字典列表'''
        obj_arr = []

        for o in objs:
            # 把Object对象转换成Dict
            dict = {}
            dict.update(o.__dict__)
            # dict['create_time']
            dict.pop("_state", None)  # 去除掉多余的字段
            time = dict['create_time'].timetuple()

            dict['create_time'] = str(time[0])+'年' + str(time[1])+"月"+str(time[2])+"日" + " " + dict['create_time'].strftime("%H:%M")
            obj_arr.append(dict)

        return obj_arr

class MySeachView(SearchView):
    template = 'search/search.html'
    def extra_context(self):       #重载extra_context来添加额外的context内容
        context = super(MySeachView,self).extra_context()
        side_list = models.Article.objects.filter(is_delete=0).count()
        context['number'] = side_list
        # print(side_list)
        return context

# @csrf_exempt
# class DetectPic(View):
#
#     @csrf_exempt
#     def post(self, request):
#         content = request.POST
#         a = 1
#         pass


@csrf_exempt
def capture(request):
    content = request.POST
    content = dict(content)
    name, contents = list(content.items())[0]
    # a = 1
    with open("media/data/images/{}".format(name), 'wb') as f:
        f.write(b64decode(contents[0]))
    # opt = parse_opt("media/data/images/{}".format(name))
    # opt = parse_opt(img_path="media/data/images/{}".format(name))
    # code = main(opt)
    cmd = r"python media/yolov5/detect.py --source media/data/images/{}".format(name)
    code = os.popen(cmd).readlines()[-1]
    # print(text)
    # pass
    return JsonResponse({
        "code": code.strip()
    })

