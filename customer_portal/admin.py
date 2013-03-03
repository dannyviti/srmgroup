from django.contrib import admin

from adminfiles.admin import FilePickerAdmin

from srmgroup.customer_portal.models import *

class FilesAdmin(FilePickerAdmin):
	adminfiles_fields = ['file_inc',]

admin.site.register(Files, FilesAdmin)

