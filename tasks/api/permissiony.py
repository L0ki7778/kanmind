from rest_framework.permissions import BasePermission
from boards.models import Board
from tasks.models import Task

class IsPartOfBoard(BasePermission):
    
    # def has_permission(self, request, view):
        
        
        
    def has_object_permission(self, request, view, obj):
        task : Task = obj
        board_id = request.data.get("board")
        try:
            board = Board.objects.get(pk = board_id)
        except:
            return False
        
        if request.method == "DELETE":
            return bool(request.user == board.owner | request.user == task.creator)
        
        return request.user == board.owner or request.user in board.members.all()