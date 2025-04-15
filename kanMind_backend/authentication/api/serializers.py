from rest_framework import serializers
from django.contrib.auth.models import User


class SimpleUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model= User
        fields = ["id", "full_name", "email"]

    def get_full_name(self,obj):
        return f'{obj.username} {obj.last_name}'.strip()


class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repeated_password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        password = self.validated_data["password"]
        repeated_password = self.validated_data["repeated_password"]

        if password != repeated_password:
            raise serializers.ValidationError({"error":"Fehler noch befüllen"})

        account = User(email = self.validated_data["email"], username = self.validated_data["username"])
        account.set_password(password)
        account.save()
        return account

    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError({"error":"Diese Email-Adresse ist bereits vergeben"})
        return value
