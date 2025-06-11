from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class PkToUserInstaceSerializer(serializers.Serializer):
    fullname = serializers.SerializerMethodField()
    id = serializers.IntegerField()
    email = serializers.EmailField()
    
    def get_fullname(self,instance):
        return f'{instance.username} {instance.last_name}'.strip()


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    fullname = serializers.CharField()

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'repeated_password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs) -> User:
        password = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']

        if password != repeated_pw:
            return serializers.ValidationError({"error: ": "Die Passwörter stimmen nicht überein"})

        names = self.validated_data['fullname'].strip().split()
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ''

        account = User(
            email=self.validated_data['email'], username=first_name, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.save()
        return account

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            return serializers.ValidationError({"error": "die Mailadresse ist bereits vergeben"})
        return value


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(label='Password', style={
                                     'input-type': 'password'}, trim_whitespace=False)

    def validate(self, obj):
        email, password = obj.get("email"), obj.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    {'Error': 'Kein User mit dieser Email-Adresse vorhanden'})
            user = authenticate(username=user.username, password=password)
            if not user:
                raise serializers.ValidationError(
                    {'Error': 'Passwort oder Email falsch'})
        else:
            raise serializers.ValidationError(
                {'Error': 'Bitte gültige Email und Passwort eingeben'})
        obj['user'] = user
        return obj
