from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source="user.id"
    )  # Solo lectura (no se envía desde frontend)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Place
        fields = "__all__"
