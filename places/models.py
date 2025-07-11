# places/models.py
from django.db import models

from users.models import CustomUser  # Asegúrate que el modelo personalizado esté aquí

from .utils import place_image_upload_path


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50, blank=True
    )  # Ej: "restaurant" para FontAwesome


class Place(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0.0)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )  # 👈 este es el campo faltante
    created_at = models.DateTimeField(auto_now_add=True)  # 👈 este campo es necesario
    image = models.ImageField(
        upload_to=place_image_upload_path,
        null=True,
        blank=True,
        default="defaults/default_place_cover.jpg",
    )

    def __str__(self):
        return self.name
