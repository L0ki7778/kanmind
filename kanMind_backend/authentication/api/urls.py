from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ResgistrationView

urlpatterns = [
    path('registration/', ResgistrationView.as_view(), name="registration"),
    path('login/', obtain_auth_token, name='login')
]
