from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permite que solo el autor de la reseña la edite o elimine.
    Otros usuarios solo pueden ver (lectura).
    """

    def has_object_permission(self, request, view, obj):
        # Lectura está permitida para cualquiera
        if request.method in permissions.SAFE_METHODS:
            return True

        # Escritura solo si el usuario es el autor
        return obj.user == request.user
