from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin
from ..models import Board
from .serializers import BoardSerializer

class BoardListCreateView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
class BoardSingleView(RetrieveUpdateDestroyAPIView):
    queryset=Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field = 'id'
    
