import json

from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsUserOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            request_data = json.loads(request.body)
            username = request_data['username']
            user = User.objects.get(username=username)
            if request.user == user:
                return True
            else:
                return False
