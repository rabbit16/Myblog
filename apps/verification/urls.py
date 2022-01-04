from django.urls import path
from verification import views

app_name = 'verification'
urlpatterns = [
    # path('pics/', views.pic_first, name='first_register'),
    path('pics/<uuid:img_codes>/', views.ImageCode.as_view(), name='register')
]