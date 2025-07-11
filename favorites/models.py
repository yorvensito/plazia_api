# favorites/models.py
from django.db import models

from places.models import Place
from users.models import CustomUser


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 👈 este campo es necesario

    class Meta:
        unique_together = ("user", "place")
