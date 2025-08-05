from rest_framework.permissions import SAFE_METHODS,BasePermission
from django.contrib.auth.models import User
from ..models import Board
from rest_framework.response import Response
from rest_framework import status


class IsOwnerOrAuthenticated(BasePermission):

    def has_permission(self, request, view)->bool:
        user:User = request.user
        board : Board = Board.objects.get(pk=view.kwargs['id'])
        method : str= request.method
        if method in SAFE_METHODS:
            return True
        return bool(user == board.owner or user in board.members.all())
    
    def has_object_permission(self, request, view, obj)->bool:
        user: User = request.user
        board : Board = obj
        method : str= request.method
        
        if method == "DELETE":
            return bool(user and user == board.owner)
        return bool(user == board.owner or user in board.members.all())
        
            