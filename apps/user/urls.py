from django.urls import path
from user import views
app_name = 'user'
urlpatterns = [
    path('', views.Index.as_view(), name ='enter'),
    # path('intro/', views.Intro.as_view(), name ='intro'),
    # path('article/', views.ContextShow.as_view(), name ='article'),
]