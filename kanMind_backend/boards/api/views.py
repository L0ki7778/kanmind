from rest_framework.generics import ListCreateAPIView,GenericAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin
from ..models import Board
from .permissions import IsOwnerOrAuthenticated
from .serializers import BoardSerializer,SingleBoardSerializer

class BoardListCreateView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
class BoardSingleView(RetrieveUpdateDestroyAPIView):
    queryset=Board.objects.all()
    serializer_class = SingleBoardSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrAuthenticated]
    
