from django.urls import path
from .views import RegisterView, MeuPerfilView, ChangePasswordView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenBlacklistView)

app_name = 'autenticacao'  # Define o namespace do conjunto de URLs como 'autenticacao'

# Lista de URLs relacionadas à autenticação e gerenciamento de usuários.
urlpatterns = [
    # Rota para registrar um novo usuário. Usa a view 'RegisterView'.
    path('signup/', RegisterView.as_view(), name='signup'),

    # Rota para acessar ou atualizar o perfil do usuário logado. Usa a view 'MeuPerfilView'.
    path('meuperfil/', MeuPerfilView.as_view(), name='meuperfil'),

    # Rota para obtenção de um novo token JWT ao realizar login. Usa a view 'TokenObtainPairView' do JWT.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Rota para renovar o token JWT com base no 'refresh token'. Usa a view 'TokenRefreshView' do JWT.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rota para fazer logout, colocando o token no blacklist. Usa a view 'TokenBlacklistView' do JWT.
    path('logout/', TokenBlacklistView.as_view(), name='logout'),

    # Rota para alterar a senha do usuário logado. Usa a view 'ChangePasswordView'.
    path('alterar-senha/', ChangePasswordView.as_view(), name='alterar-senha'),
]
