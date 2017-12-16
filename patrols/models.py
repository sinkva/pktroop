from django.db import models
# from scouts.models import Profile
from django.contrib.auth.models import User


# Create your models here.

class Patrol(models.Model):
    patrol_name = models.CharField(max_length=50)
    patrol_members = models.ManyToManyField(User, through='Patrol_Membership')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patrol_name

class Patrol_Membership(models.Model):
    scout = models.ForeignKey(User, on_delete=models.CASCADE)
    patrol = models.ForeignKey(Patrol, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_left = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

