from django.contrib import admin
from apps.index.models import User, UserManager

# Register your models here.
admin.site.register(User)
# admin.site.register(UserManager)