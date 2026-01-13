from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    profile_pic = models.ImageField(upload_to="profiles", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username}"
