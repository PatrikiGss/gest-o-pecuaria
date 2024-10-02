from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True) 
    telefone = models.CharField(max_length=15)
    # senha = models.CharField(max_length=128) usar o campo password padrao do django
    creditos = models.IntegerField()

    username = None  # Removendo o campo username
    USERNAME_FIELD = 'email'  # Definindo o email como campo de login
    REQUIRED_FIELDS = []  # Define campos obrigatorios

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return str(self.nome)