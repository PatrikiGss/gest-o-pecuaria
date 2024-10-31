from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True) 
    telefone = models.CharField(max_length=15)
    creditos = models.IntegerField()

    username = None  
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return str(self.nome)