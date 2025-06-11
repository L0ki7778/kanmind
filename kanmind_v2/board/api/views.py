from rest_framework import generics
from .serializers import BoardCreateSerializer
from ..models import Board
from django.db import models
from .permissions import IsBoardOwnerOrBoardMember


class BoardListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsBoardOwnerOrBoardMember]
    serializer_class = BoardCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(
            models.Q(owner=user) | models.Q(members=user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save()
