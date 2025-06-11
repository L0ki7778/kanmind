from rest_framework import generics
from ..models import Task
from .serializers import TaskModelSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task
    serializer_class = TaskModelSerializer
    pass
