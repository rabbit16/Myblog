import json

from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.utils import timezone
from django.views import View
from leacots.models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

page_every_show = 5

class ShowLeactos(View):
    def get(self, request):
        if request.GET.get('page'):
            page_now = int(request.GET.get('page'))
        else:
            page_now = 1
        all_comments = Leacots.objects.filter(is_delete=False)
        all_objs = Paginator(all_comments, page_every_show)
        page_num = all_objs.num_pages
        comments_num = all_objs.count
        if page_now > page_num:
            page_now = page_num
        if page_now <= 1:
            page_now = 1
        return_objs = Paginator(all_comments, page_every_show).get_page(page_now)
        content_dict = {
            "page_num": page_num,
            "comments": return_objs,
            "comments_num": comments_num,
            "page_now": page_now,
            "every_page_show": page_every_show,
            "all_num": all_objs.count
        }
        return render(request, 'leacots/leacots.html', context=content_dict)

    @csrf_exempt
    def post(self, request):
        add_data = json.loads(request.body)
        user_id = Leacots.objects.all().count()
        if user_id == 0:
            user_id = 1
        else:
            user_id += 1
        create_time = timezone.now()
        if add_data['name'] == '':
            return JsonResponse({"fail": "名称不能为空"})
        Leacots.objects.create(
            id=user_id,
            create_time=create_time,
            update_time=create_time,
            is_delete=False,
            name=add_data['name'],
            content=add_data['context']
        )

        return JsonResponse({"success": 200})

