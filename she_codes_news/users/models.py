from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

def __str__(self):
    return self.username


class UserProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.FileField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username