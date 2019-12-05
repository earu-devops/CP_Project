#This urls.py file is under UserRegApp1 Folder

from django.urls import path
from django.contrib import admin
from UserRegApp1 import views as UserRegApp1_views

urlpatterns = [
 path('userdetails/', UserRegApp1_views.UserRegView),
 path('display/', UserRegApp1_views.UserRegView),
 #path('', admin.site.urls),
]
