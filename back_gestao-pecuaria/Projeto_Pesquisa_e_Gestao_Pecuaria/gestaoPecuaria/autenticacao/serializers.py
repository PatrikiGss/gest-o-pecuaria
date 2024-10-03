from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
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

        # Busca o modelo de usuário
        Usuario = get_user_model()

        # Tenta buscar o usuário pelo email
        user = Usuario.objects.filter(email=email).first()
        
        if user is None:
            raise serializers.ValidationError(_('Usuário não encontrado com este email.'), code='authorization')

        # Verifica se a senha está correta
        if not user.check_password(password):
            raise serializers.ValidationError(_('Credenciais inválidas.'), code='authorization')

        if not user.is_active:
            raise serializers.ValidationError(_('Esta conta está inativa.'), code='authorization')

        # Se tudo estiver correto, retorna o usuário validado
        attrs['user'] = user
        return attrs
    