from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions

from .models import CustomUser
from .serializers import UserSerializer


@extend_schema(
    tags=["Users"],
    summary="Perfil de usuario autenticado",
    description="Devuelve y permite actualizar el perfil del usuario autenticado.",
)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
