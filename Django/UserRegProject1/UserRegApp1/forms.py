#This forms.py file is under UserRegApp1

from django.forms import ModelForm
from UserRegApp1.models import UserRegModel

class UserRegModelForm(ModelForm):
    #username = forms.CharField(label = 'Username', max_length=30)
    #emailid = forms.EmailField(label='Email', max_length=100, help_text= 'Required')
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    #password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    class Meta:
        model = UserRegModel
        fields = ('username', 'emailid', 'password1', 'password2')
