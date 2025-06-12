from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, EmailAuthTokenSerializher
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
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
                'fullname': f'{saved_account.username} {saved_account.last_name}',
                'email': saved_account.email,
                'id':saved_account.id
            }
        else:
            data = serializer.errors
        return Response(data)
    

class CustomLoginView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializher
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        data = {}
        if serializer.is_valid():
            saved_account:User = serializer.validated_data['user']
            token:Token = Token.objects.get(user = saved_account)
            data = {
                'token':token.key,
                'fullname':f'{saved_account.username} {saved_account.last_name}',
                'email':saved_account.email,
                'user_id':saved_account.pk
            }
        else:
            data = serializer.errors
        return Response(data)
        
    