from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.contrib.auth.hashers import check_password

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        # Busca o modelo de usuário
        Usuario = get_user_model()

        # Tenta buscar o usuário pelo email
        user = Usuario.objects.filter(email=email).first()

        if user is None:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se a senha está correta
        if not check_password(password, user.password):
            return Response({"error": "Senha incorreta."}, status=status.HTTP_400_BAD_REQUEST)

        # Gera ou obtém o token para o usuário autenticado
        token, created = Token.objects.get_or_create(user=user)# pylint: disable=no-member

        # Retorna uma resposta customizada com o token
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        }, status=status.HTTP_200_OK)


# View para logout
class LogoutView(APIView):
    def post(self, request):
        request.auth.delete()  # Apaga o token do usuário atual
        return Response({"detail": "Logout realizado com sucesso."}, status=200)
