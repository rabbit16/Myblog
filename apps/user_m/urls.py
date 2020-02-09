from django.urls import path

from user_m import views
app_name = 'user_m'
urlpatterns = [
    path('register/',views.Register.as_view(),name = 'register')
]