from django.contrib import admin
from django.db import models as mdl
# Register your models here.
from blog import models

admin.site.register(models.Tag)

from mdeditor.widgets import MDEditorWidget


class ExampleModelAdmin (admin.ModelAdmin):
    formfield_overrides = {
        mdl.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(models.Article, ExampleModelAdmin)

