from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.permissions import IsOwnerOrReadOnly

from .models import Place
from .serializers import PlaceSerializer


@extend_schema(
    tags=["Places"],
    summary="Lugares de interés",
    description="Permite listar, ver, crear, actualizar y eliminar lugares de interés.",
)
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "created_at", "is_active"]
    search_fields = ["name", "description", ]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-rating"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="Lugares del usuario actual",
        description="Retorna los lugares creados por el usuario autenticado.",
        tags=["Places"],
        responses={200: PlaceSerializer(many=True)},
    )
    @action(
        detail=False,
        methods=["get"],
        url_path="mine",
        permission_classes=[permissions.IsAuthenticated],
    )
    def mine(self, request):
        user_places = Place.objects.filter(user=request.user)
        serializer = self.get_serializer(user_places, many=True)
        return Response(serializer.data)
