from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

def __str__(self):
    return self.username

# could add in avatars and urls