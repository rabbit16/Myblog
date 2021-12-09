from django.test import TestCase

# Create your tests here.
# class ArticleNextPage(View):
#     def get(self, request, tag_page):
#         flag = 0
#         final_flag = 0
#         first_flag = 0
#         if '+' in tag_page:
#             tag_page.replace('+', '-')
#             final_flag = 1
#         if '=' in tag_page:
#             first_flag = 1
#         if '--' in tag_page:
#             flag = 1
#             page_num, tag_id = [int(i) for i in tag_page.split('--')]
#         else:
#             if final_flag:
#                 page_num, tag_id = [int(i) for i in tag_page.split('+')]
#             elif first_flag:
#                 page_num, tag_id = [int(i) for i in tag_page.split('=')]
#             else:
#                 page_num, tag_id = [int(i) for i in tag_page.split('-')]
#         tag_name = models.Tag.objects.all()[tag_id - 1].tag_name
#         articles = models.Article.objects.filter(tags__name__in=[tag_name])
#         all_num = models.Article.objects.filter(tags__name__in=[tag_name]).count()
#         page_all = math.ceil(all_num / page_show_num)
#         first_page = [2, tag_id]
#         final_page = [page_all+1, tag_id]
#         if flag == 1:
#             page_num = page_num - 1
#         else:
#             if final_flag or first_flag:
#                 pass
#             else:
#                 page_num = page_num + 1
#
#         if page_num <= 1 or page_num > (page_all+1):
#             page_num = 2
#         try:
#             articles = articles[(page_num - 2) * page_show_num: (page_num-1) * page_show_num]
#         except:
#             articles = articles[(page_num - 2) * page_show_num:]
#         page_tag_list = [page_num, tag_id]
#         articles_dict = {
#             'articles': articles,
#             'page_num': page_all,
#             'all_num': all_num,
#             'page_now': page_num,
#             'tag_id': tag_id,
#             'page_tag_list': page_tag_list,
#             'final_page': final_page,
#             'first_page': first_page,
#             'every_page_show': page_show_num
#         }
#         # return render(request, 'message/article_list.html', context=articles_dict)
#         return render(request, 'message/article_next_page.html', context=articles_dict)