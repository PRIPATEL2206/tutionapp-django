from rest_framework import permissions
from rest_framework.request import Request
from django.contrib.auth.models import User

class IsAdminOrReadPermission(permissions.BasePermission):

    def has_permission(self, request:Request, view):
        if request.method == 'POST' and not request.user.is_superuser:
            return False
        return True