from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer
from .models import Usuario
from rest_framework.permissions import AllowAny, IsAuthenticated

# View para registro de novos usuários
class RegisterView(generics.CreateAPIView):
    """
    View responsável por permitir o registro (criação) de novos usuários.
    Usa o método POST.
    """
    queryset = Usuario.objects.all()  # Define o conjunto de usuários disponíveis
    serializer_class = UsuarioSerializer  # Define o serializer usado para validação e criação
    permission_classes = [AllowAny]  # Qualquer pessoa pode acessar este endpoint para registrar

# View para login
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View responsável por gerar o token JWT para login de usuários.
    Pode ser personalizada se necessário.
    """
    pass  # Por enquanto, está usando a implementação padrão do TokenObtainPairView

# View para obter, atualizar ou excluir um usuário existente
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View responsável por:
    - Obter as informações do usuário logado (método GET)
    - Atualizar os dados do usuário logado (método PUT ou PATCH)
    - Excluir o usuário logado (método DELETE)
    """
    queryset = Usuario.objects.all()  # Conjunto de todos os usuários
    serializer_class = UsuarioSerializer  # Define o serializer usado para serializar/deserializar dados
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar essa view

    def get_object(self):
        #Sobrescreve o método get_object para garantir que o usuário só possa acessar, editar ou excluir sua própria conta.
        return self.queryset.get(pk=self.request.user.pk)  # Retorna o usuário logado

