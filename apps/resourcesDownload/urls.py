from django.contrib import admin
from django.urls import include, path
from resourcesDownload import views

app_name = 'resource'
urlpatterns = [
    path('', views.Resource.as_view(), name='downloadP'),
    path('page/<int:page_num>', views.ResourcePageShow.as_view(), name='page_change'),
    # path('page_back/<int:page_num>', views.ResourcePageJianShow.as_view(), name='page_back')
]