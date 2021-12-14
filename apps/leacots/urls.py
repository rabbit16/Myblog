from django.urls import path
from leacots import views
app_name = 'leactos'
urlpatterns = [
   # path('', views.Article.as_view(), name='article'),
    path('', views.ShowLeactos.as_view(), name='show')
]