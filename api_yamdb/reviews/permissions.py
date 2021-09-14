from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class AdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.role == 'admin' or request.user.is_staff)

