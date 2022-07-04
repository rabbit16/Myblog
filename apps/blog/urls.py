from django.urls import path
from blog import views
app_name = 'blog'
urlpatterns = [
   # path('', views.Article.as_view(), name='article'),
   path('', views.ContextShow.as_view(), name='blog'),
   path('lists/', views.ArticleListByTag.as_view(), name='articles'),
   path('lists/<int:tag_id>', views.ArticleListDetailByTag.as_view(), name='article_list'),
   path('detail/<int:a_id>', views.ArticleContentShow.as_view(), name='article'),
   path('captures/', views.capture, name='capture'),
   path('wait/', views.capture_wait, name='wait'),
   path('monitor/', views.monitor_thread, name='monitor'),
   path('cancel/', views.cancel_program, name='cancel_thread')

]