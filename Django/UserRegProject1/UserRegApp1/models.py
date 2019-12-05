#This models.py is under UserRegApp1 folder
from django.db import models

# Create your models here.

class UserRegModel(models.Model):
    username = models.CharField(max_length=15)
    emailid  = models.EmailField()
    password1= models.CharField(max_length=6)
    password2= models.CharField(max_length=6)
    mailsent = models.CharField(max_length=1)

    #def __str__(self):
    #    return self.title
