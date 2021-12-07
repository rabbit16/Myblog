from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.Index.as_view(), name='enter'),
    # path('intro/', views.Intro.as_view(), name ='intro'),
    # path('article/', views.ContextShow.as_view(), name ='article'),
]