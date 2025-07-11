from django.db import models

from places.models import Place
from users.models import CustomUser


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
