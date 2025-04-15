from rest_framework.generics import ListCreateAPIView
from .seriralizers import TaskListCreateSerializer
from ..models import Task

class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListCreateSerializer
