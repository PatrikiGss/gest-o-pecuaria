from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# View para login
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Chama o método post original para autenticar o usuário
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)# pylint: disable=no-member
        
        # Retorna uma resposta customizada com informações adicionais
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })

# View para logout
class LogoutView(APIView):
    def post(self, request):
        request.auth.delete()  # Apaga o token do usuário atual
        return Response({"detail": "Logout realizado com sucesso."}, status=200)
