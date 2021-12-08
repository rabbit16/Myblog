from django.shortcuts import render
from django.views import View
from blog  import models
import markdown
# Create your views here.

class Article(View):
    def get(self, request):
        news = models.Article.objects.filter(is_delete=False)[0]
        return render(request, 'message/../../templates/废了/articles.html', context={
            'news': news
        })

class ContextShow(View):
    def get(self, request):
        articles = models.Article.objects.filter(is_delete=False)
        try:
            articles = articles[0:5]  # 首页就展示前10个文章
        except:
            articles = articles[0:]
        return render(request,'message/article_first.html', context={
            'articles': articles
        })

class ArticleContentShow(View):
    def get(self, request, a_id):
        news = models.Article.objects.filter(is_delete=False)[a_id-1]
        news.content = markdown.markdown(news.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            'markdown.extensions.toc'  # 自动生成目录
        ])  # 修改blog.content内容为html
        return render(request, 'message/article_detail.html', context={
            'article': news
        })
        # pass