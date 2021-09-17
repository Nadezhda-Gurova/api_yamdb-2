from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    bio = models.TextField(
        max_length=1000,
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
