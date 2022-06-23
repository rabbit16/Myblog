from django.contrib import admin
from django.db import models as mdl
# Register your models here.
from blog import models



from mdeditor.widgets import MDEditorWidget


# class TagSelectAdmin(admin.ModelAdmin):
#     list_display = ('tag_name',)
#     fieldsets = ((None, {'fields': ('tag_id','tag_name', 'img_url')}),)
#     filter_horizontal = ('articles',)

class ExampleModelAdmin (admin.ModelAdmin):
    formfield_overrides = {
        mdl.TextField: {'widget': MDEditorWidget}
    }
admin.site.register(models.Tag)
admin.site.register(models.AuthorAndTag)
admin.site.register(models.Article, ExampleModelAdmin)

