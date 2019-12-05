#This view.py file is under UserRegApp1

from django.shortcuts import render
from django.db import models
from .models import UserRegModel
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import UserRegModelForm

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def UserRegView(request):
    #return HttpResponse(request.method)
    if request.method == 'POST':
        form = UserRegModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            context_object_name = 'user_list'
            user_list = UserRegModel.objects.all()
            #to get a entered emailid value
            receiver_mail_id = UserRegModel.objects.only('emailid').get(id=66).emailid
            lv_username = UserRegModel.objects.only('username').get(id=66).username

            #send confirmation mail to user
            send_mail('Verification Email Sent to ' + lv_username, 'Thank you for registering to our site', settings.EMAIL_HOST_USER, [receiver_mail_id,])

            UserRegModel.objects.only('mailsent').update(mailsent='Y')
            #UserRegModel.objects.filter(username = "TEST1").update(mailsent="Y")
            u = form.save()
            #lv_mailsent =  UserRegModel.objects.filter(username = "TEST1", mailsent = "Y")
            lv_mailsent = UserRegModel.objects.only('mailsent').get(id=66).mailsent

            if lv_mailsent == 'Y':
                return render(request, 'display.html', {'UsersKey' : user_list})
            else:
                return HttpResponse('<h1> email not verified </h1>')

    else:
        form_class = UserRegModelForm

    return render(request, 'userdetails.html', {'FormKey' : form_class})
