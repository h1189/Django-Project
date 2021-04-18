from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WebAppUser,File
from  django.contrib.auth.models import User

class WebAppUserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_admin']

class FileAdmin(admin.ModelAdmin):
    list_display = ['username','date_of_file_upload']


admin.site.register(WebAppUser, WebAppUserAdmin)
admin.site.register(File,FileAdmin)