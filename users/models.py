from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    aadhar = models.CharField(max_length=12, blank=False,null=True)
    phone = models.CharField(max_length=10, blank=False,null=True)