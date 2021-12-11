
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.username}'


