from django.db import models
from django.contrib.auth.models import User

College_CHOICES = (
        (None,'Please Select Your College'),
        ('Veermata Jijabai Technological Institute','Veermata Jijabai Technological Institute'),
        ('Sardar Patel Institute of Technology','Sardar Patel Institute of Technology'),
        ('KJ Somaiya College of Engineering','KJ Somaiya College of Engineering'),
        ('Dwarkadas J Sanghvi College of Engineering','Dwarkadas J Sanghvi College of Engineering'),
        ('Sardar Patel College of Engineering','Sardar Patel College of Engineering'),
        ('Thadomal Shahani Engineering College','Thadomal Shahani Engineering College'),
        ('Vivekanand Education Societys Institute of Technology','Vivekanand Education Societys Institute of Technology'),
        ('KJ Somaiya Institute of Engineering and Information Technology','KJ Somaiya Institute of Engineering and Information Technology'),
        )
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    stu_id = models.IntegerField(null=True)
    mob_num = models.IntegerField(null=True)
    course = models.TextField(null=True)
    year = models.TextField(null=True)
    stu_col = models.TextField(null=True, choices=College_CHOICES)
    is_faculty = models.BooleanField(default=False)
    