from rest_framework import serializers
from .models import Usuario

# Serializador principal para o modelo Usuario, utilizando todos os campos.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # Define o modelo que será utilizado pelo serializador.
        fields = "__all__"  # Utiliza todos os campos do modelo.
        extra_kwargs = {
            'password': {'write_only': True}  # Garante que o campo 'password' seja apenas para escrita e não retornado nas respostas.
        }

    # Método para criar um novo usuário.
    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Remove a senha do dicionário de dados validados.
        instance = self.Meta.model(**validated_data)  # Cria a instância do modelo com os dados validados restantes.
        if password is not None:
            instance.set_password(password)  # Criptografa a senha antes de salvar.
        instance.save()  # Salva a instância no banco de dados.
        return instance

    # Método para atualizar um usuário existente.
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Remove a senha do dicionário de dados validados.
        if password:
            instance.set_password(password)  # Atualiza a senha com criptografia, se foi fornecida uma nova senha.
        return super().update(instance, validated_data)  # Atualiza a instância do usuário com os outros campos validados.

# Serializador para atualização parcial do usuário.
class UpdateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'email']  # Apenas os campos permitidos para atualização são listados.

# Serializador para leitura (consulta) do usuário.
class GetUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'email']  # Apenas os campos que devem ser exibidos na consulta.

# Serializador para alteração de senha do usuário.
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)  # Campo para a senha atual do usuário.
    new_password = serializers.CharField(required=True)  # Campo para a nova senha que o usuário deseja definir.

    # Validação personalizada da senha antiga.
    def validate_old_password(self, value):
        user = self.context['request'].user  # Obtém o usuário atual do contexto da requisição.
        if not user.check_password(value):  # Verifica se a senha antiga fornecida está correta.
            raise serializers.ValidationError("Senha atual incorreta.")  # Lança erro se a senha antiga estiver incorreta.
        return value  # Retorna o valor validado da senha antiga.

    # Validações gerais para a troca de senha.
    def validate(self, attrs):
        if attrs['old_password'] == attrs['new_password']:  # Verifica se a nova senha é igual à antiga.
            raise serializers.ValidationError("A nova senha não pode ser igual à senha atual.")  # Erro se as senhas forem iguais.
        return attrs  # Retorna os atributos validados.
