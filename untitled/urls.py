"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from untitled import settings, pre_settings
from django.conf.urls.static import static
from django.conf.urls import url

##新增
urlpatterns = [
                  path('rabbit/', admin.site.urls),
                  path('', include('index.urls')),

                  path('', include('verification.urls')),
                  path(r'search/', include('haystack.urls')),
                  url(r'^static/(?P<path>.*)$',
                      serve,
                      {
                          'document_root': pre_settings.STATICFILES_DIRS[0]
                          # 'document_root': settings.STATIC_ROOT
                      },
                      name='static'
                      ),
                  path('article/', include('blog.urls')),
                  path('resources/', include('resourcesDownload.urls')),
                  re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  path('notification/', include('notification.urls')),
                  path('leactos/', include('leacots.urls')),
                  path('mdeditor/', include('mdeditor.urls')),
                  # path('index/', include('user_m.urls')),
                  # path('', include('verifications.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
