# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    avatar = models.ImageField(
        upload_to="users/avatars/%Y/%m/%d/",
        null=True,
        blank=True,
        default="defaults/default_profile_icon.jpg",
    )
