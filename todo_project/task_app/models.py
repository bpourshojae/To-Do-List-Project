from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=264,blank=False)
    description = models.TextField(blank=False)
    status = models.BooleanField(blank=True,default=False)
    
