from django.urls import path
from verification import views

app_name = 'verification'
urlpatterns = [
    path('', views.pics)
]