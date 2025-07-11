from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.permissions import IsOwnerOrReadOnly

from .models import Review
from .serializers import ReviewSerializer


@extend_schema(
    tags=["Reviews"],
    summary="Reseñas de lugares",
    description="Permite ver y crear reseñas sobre los lugares por parte de usuarios autenticados.",
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Reseñas del usuario actual",
        description="Devuelve las reseñas creadas por el usuario autenticado.",
        tags=["Reviews"],
        responses={200: ReviewSerializer(many=True)},
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="mine",
        permission_classes=[permissions.IsAuthenticated],
    )
    def mine(self, request):
        user_reviews = Review.objects.filter(user=request.user)
        serializer = self.get_serializer(user_reviews, many=True)
        return Response(serializer.data)
