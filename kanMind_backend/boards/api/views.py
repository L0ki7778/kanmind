from rest_framework.generics import ListCreateAPIView
from ..models import Board
from .serializers import BoardSerializer

class BoardListCreateView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
