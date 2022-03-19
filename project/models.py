from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

Category_CHOICES = (
    (None, 'Select Category'),
    ('Ongoing', 'Ongoing'),
    ('Complete', 'Complete'),
    ('Incomplete', 'Incomplete'),
    ('Research', 'Research'),
)


class Project(models.Model):
    title = models.CharField(max_length=128)
    statement = models.CharField(max_length=256)
    domain = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=Category_CHOICES)
    institute = models.CharField(max_length=256, default=NULL)
    is_approved = models.BooleanField(default=False)
    plagarised = models.FloatField(null=True)
    plagarised_with = models.CharField(max_length=128, blank=True, null=True)
    # user info
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/project-detail/{self.id}/"
