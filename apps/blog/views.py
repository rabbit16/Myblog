import json
import math

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from blog import models
import markdown
# Create your views here.
page_show_num = 4
tag_show_num = 8
class ContextShow(View):
    def get(self, request):
        articles = models.Article.objects.filter(is_delete=False)
        try:
            articles = articles[0:page_show_num]  # 首页就展示前page_show_num个文章
        except:
            articles = articles[0:]
        return render(request,'message/article_first.html', context={
            'articles': articles
        })

class ArticleContentShow(View):
    def get(self, request, a_id):
        news = models.Article.objects.filter(is_delete=False).reverse()[a_id-1]
        news.content = markdown.markdown(news.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            'markdown.extensions.toc'  # 自动生成目录
        ])  # 修改blog.content内容为html
        return render(request, 'message/article_detail.html', context={
            'article': news
        })

class ArticleListByTag(View):
    def get(self, request):
        tag = models.Tag.objects.all()[:tag_show_num]
        all_obj = models.Tag.objects.count()
        pag_num = math.ceil(models.Tag.objects.count() / tag_show_num)
        now_page = 1
        tag_dict = {
            'tags': tag,
            'page_num': pag_num,
            'all_num': all_obj,
            'now_page': now_page
        }
        return render(request, 'message/article_tag_list.html', context=tag_dict)

class ArticleListDetailByTag(View):
    @csrf_exempt
    def get(self, request, tag_id):
        tag_name = models.Tag.objects.filter(tag_id=tag_id)[0].tag_name
        articles = models.Article.objects.filter(tags__name__in=[tag_name])[:page_show_num]
        articles_count = models.Article.objects.filter(tags__name__in=[tag_name]).count()
        page_num = math.ceil(articles_count/page_show_num)
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
        tag_name = models.Tag.objects.all()[tag_id-1].tag_name
        all_num = models.Article.objects.filter(tags__name__in=[tag_name]).count()
        page_all = math.ceil(all_num / page_show_num)
        page_num = json.loads(request.body)
        page_num = int(page_num['page_num']) + 1
        try:
            final_page_flag = json.loads(request.body)['final']
        except:
            pass
        if (page_num <= 0 or page_num > page_all) and final_page_flag != 1:
            page_num = 1
        if final_page_flag:
            page_num = page_all
        try:
            articles = models.Article.objects.filter(tags__name__in=[tag_name])[(page_num - 1) * page_show_num: page_num * page_show_num]
        except:
            articles = models.Article.objects.filter(tags__name__in=[tag_name])[(page_num - 1) * page_show_num:]
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



