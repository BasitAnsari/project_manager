from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length= 128)
    statement = models.CharField(max_length=256)
    domain = models.CharField(max_length= 128)
    category = models.CharField(max_length= 128)
    #user info
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    