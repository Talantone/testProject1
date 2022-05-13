from rest_framework import permissions

from tasks import models


class IsOwner(permissions.BasePermission): #Permission for Owner-only updating of model objects

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
