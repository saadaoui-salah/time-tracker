from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user    = models.ForeignKey(User, related_name='userprofile', on_delete=models.CASCADE) 
    team_id = models.IntegerField(default=0)