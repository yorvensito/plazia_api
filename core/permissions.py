from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Solo el dueño del objeto puede modificarlo. Lectura abierta.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
