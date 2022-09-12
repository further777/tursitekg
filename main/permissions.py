from rest_framework.permissions import BasePermission,SAFE_METHODS
from accounts.models import userProfile
class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        userP = userProfile.objects.get(user = request.user)
        return obj.user==request.user