from django import forms
from .models import Task
from .models import UserInfo
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','status')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User  
        fields = ('username','password','email')

class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = UserInfo 
        fields = ("profile_pic","user_site")         