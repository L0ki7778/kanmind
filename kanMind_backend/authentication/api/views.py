from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ResgistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = RegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            saved_account = serializer.save()
            token = Token.objects.create(user = saved_account)
            data = {
                'token': token.key,
                'fullname': saved_account.username,
                'email': saved_account.email,
                'id':saved_account.id
            }
        else:
            data = serializer.errors
        return Response(data)
    