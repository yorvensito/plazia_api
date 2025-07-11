from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.permissions import IsOwnerOrReadOnly

from .models import Favorite
from .serializers import FavoriteSerializer


@extend_schema(
    tags=["Favorites"],
    summary="Lugares favoritos",
    description="Permite agregar, ver y eliminar lugares marcados como favoritos por el usuario.",
)
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Favoritos del usuario actual",
        description="Retorna los lugares marcados como favoritos por el usuario autenticado.",
        tags=["Favorites"],
        responses={200: FavoriteSerializer(many=True)},
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="mine",
        permission_classes=[permissions.IsAuthenticated],
    )
    def mine(self, request):
        user_favorites = Favorite.objects.filter(user=request.user)
        serializer = self.get_serializer(user_favorites, many=True)
        return Response(serializer.data)
