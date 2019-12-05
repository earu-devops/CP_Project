#This admin.py file is under UserRegApp1

from django.contrib import admin
from UserRegApp1.models import UserRegModel

# Register your models here.

class UserRegModelAdmin(admin.ModelAdmin):
    #disply the data in admin interface
    list_display = ['id', 'username','emailid','password1','password1','mailsent']

#Register the ModelAdmin
admin.site.register(UserRegModel, UserRegModelAdmin)
