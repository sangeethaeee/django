from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
admin.site.register(Names)
class NamesAdmin(ImportExportModelAdmin)
       list_display=('Names')