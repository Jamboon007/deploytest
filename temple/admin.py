from django.contrib import admin
from .models import temple
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
class RecordAdmin(ImportExportActionModelAdmin):
    list_display=['อันดับ']
admin.site.register(temple)