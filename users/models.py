from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    stu_id = models.IntegerField(null=True)
    mob_num = models.IntegerField(null=True)
    stu_col = models.TextField(null=True)
    