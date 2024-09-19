from rest_framework import serializers
from .models import Usuario # Ajuste conforme sua estrutura
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'telefone', 'email', 'senha', 'creditos']
        extra_kwargs = {'senha': {'write_only': True}}

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])  # Criptografa a senha
        return super().create(validated_data)