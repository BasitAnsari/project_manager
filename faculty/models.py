from django.db import models
from users.models import User
# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(User,on_delete=models.CASCADE)
    gForm_link = models.CharField(max_length=256)