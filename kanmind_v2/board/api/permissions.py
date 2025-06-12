from rest_framework.permissions import BasePermission


class IsBoardOwnerOrBoardMember(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user or obj.members.filter(pk=request.user.pk).exists())
