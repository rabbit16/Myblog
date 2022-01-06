from django.urls import path, re_path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.Index.as_view(), name='enter'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.LoginOut.as_view(), name='logout'),
    # path('intro/', views.Intro.as_view(), name ='intro'),
    # path('article/', views.ContextShow.as_view(), name ='article'),
]