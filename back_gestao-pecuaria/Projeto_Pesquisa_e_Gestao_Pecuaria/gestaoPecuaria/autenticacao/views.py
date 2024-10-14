from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer, UpdateUsuarioSerializer, GetUsuarioSerializer, ChangePasswordSerializer

from .models import Usuario

# View para registro de novos usuários.
class RegisterView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)  # Serializa os dados recebidos da requisição.
        serializer.is_valid(raise_exception=True)  # Valida os dados, levantando exceção em caso de erro.
        serializer.save()  # Salva o novo usuário no banco de dados.
        return Response(serializer.data)  # Retorna os dados do usuário recém-criado como resposta.

# View para exibir e atualizar o perfil do usuário logado.
class MeuPerfilView(APIView):
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam acessar esta view.

    def put(self, request):
        try:
            user = Usuario.objects.get(pk=request.user.id)  # Obtém o usuário logado usando seu ID.
        except Usuario.DoesNotExist:# pylint: disable=no-member Caso o usuário não exista, levanta a exceção NotFound.
            raise NotFound('Usuário não encontrado.')

        # Serializa os dados do usuário para atualização parcial (somente os campos fornecidos).
        serializer = UpdateUsuarioSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)  # Valida os dados fornecidos.
        serializer.save()  # Atualiza os dados do usuário no banco de dados.
        return Response(serializer.data)  # Retorna os dados atualizados do usuário.

    def get(self, request):
        try:
            user = Usuario.objects.get(pk=request.user.id)  # Obtém o usuário logado usando seu ID.
        except Usuario.DoesNotExist:# pylint: disable=no-member Caso o usuário não exista, levanta a exceção NotFound.
            raise NotFound('Usuário não encontrado.')

        # Serializa os dados do usuário para exibição.
        serializer = GetUsuarioSerializer(user)
        return Response(serializer.data)  # Retorna os dados do usuário como resposta.

# View para permitir a alteração de senha do usuário.
class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)  # Garante que apenas usuários autenticados possam acessar esta view.

    def post(self, request, *args, **kwargs):
        # Serializa os dados da requisição, incluindo o contexto com o usuário autenticado.
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():  # Valida os dados fornecidos.
            user = request.user  # Obtém o usuário logado.
            user.set_password(serializer.validated_data['new_password'])  # Define a nova senha criptografada.
            user.save()  # Salva o usuário com a nova senha no banco de dados.
            return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)  # Retorna sucesso.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erro se a validação falhar.

# pylint: disable=no-member
