from django.urls import path, re_path
from verification import views

app_name = 'verification'
urlpatterns = [
    # path('pics/', views.pic_first, name='first_register'),
    path('pics/<uuid:img_codes>/', views.ImageCode.as_view(), name='register'),
    path('username/<username>/', views.UserNameCheck.as_view(), name='checkName'),
]