from rest_framework import serializers
from Projeto_Pesquisa_e_Gestao_Pecuaria.gestaoPecuaria.apps.core.models import Usuario  # Ajuste conforme sua estrutura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'telefone', 'email', 'senha', 'creditos']
        extra_kwargs = {'senha': {'write_only': True}}  # A senha não será exibida nas respostas

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['senha'])  # Criptografa a senha
        usuario.save()
        return usuario
