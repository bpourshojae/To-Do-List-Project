from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=264,blank=False)
    description = models.TextField(blank=False)
    status = models.BooleanField(blank=True,default=False)
    
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(blank=True,upload_to='task_app')
    user_site = models.URLField(blank=True)