from django.urls import path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.Index.as_view(), name='enter'),
    path('register/', views.Register.as_view(), name='register'),
    # path('intro/', views.Intro.as_view(), name ='intro'),
    # path('article/', views.ContextShow.as_view(), name ='article'),
]