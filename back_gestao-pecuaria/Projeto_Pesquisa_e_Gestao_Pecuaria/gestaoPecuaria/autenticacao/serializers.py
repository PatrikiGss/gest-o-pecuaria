from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields="__all__"
        extra_kwargs={
            'password': {'write_only': True}
        }
def create (self, validated_data):
    password = validated_data.pop('password')
    usuario = Usuario(**validated_data)
    usuario.set_password(password)
    usuario.save()
    return usuario


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Autentica o usuário com email e senha
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError(_('Unable to log in with provided credentials.'), code='authorization')
        else:
            raise serializers.ValidationError(_('Must include "email" and "password".'), code='authorization')

        attrs['user'] = user
        return attrs
    