from django.contrib import admin

# Register your models here.

from resourcesDownload.models import *

admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(ResourceAndTag)