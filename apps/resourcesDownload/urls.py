from django.contrib import admin
from django.urls import include, path
from resourcesDownload import views

app_name = 'resource'
urlpatterns = [
    path('', views.ResourceShow.as_view(), name='downloadP'),
    path('page/<int:page_num>', views.ResourcePageShow.as_view(), name='page_change'),
    path('page/download', views.FileDownload.as_view(), name='download'),
    path('page/<str:tag_name>', views.SpecificResource.as_view(), name='resource_list'),
    # path('page_back/<int:page_num>', views.ResourcePageJianShow.as_view(), name='page_back')
]