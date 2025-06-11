from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, EmailLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = RegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            saved_account = serializer.save()
            print("das ist ein print",saved_account)
            token = Token.objects.create(user = saved_account)
            data = {
                'token':token.key,
                'fullname':f'{saved_account.username} {saved_account.last_name}',
                'email':saved_account.email,
                'id':saved_account.id
            }
        else:
            data = serializer.errors
        return Response(data)
    

class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = EmailLoginSerializer
    
    def post(self, request):
        serializer  = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            account = serializer.validated_data['user']
            token = Token.objects.get(user = account)
            data = {
                'token':token.key,
                'fullname':f'{account.first_name} {account.last_name}',
                'email':account.email,
                'user_id':account.id
            }
        else:
            data= serializer.errors
        return Response(data)