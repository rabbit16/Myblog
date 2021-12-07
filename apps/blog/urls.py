from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
   # path('', views.Article.as_view(), name='article'),
   path('', views.ContextShow.as_view(), name='blog'),
   path('detail/<int:a_id>', views.ArticleContentShow.as_view(), name='article'),
]