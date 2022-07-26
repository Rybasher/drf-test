from rest_framework import permissions


class PermissionAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in ('DELETE'):
            return True
        return bool(request.user and request.user.is_staff)