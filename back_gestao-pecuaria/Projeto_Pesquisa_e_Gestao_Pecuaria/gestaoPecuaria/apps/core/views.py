from rest_framework import viewsets
from django.db import models
from .models import Usuario,Produtor,Propriedade,Laboratorio,Cultura,AnaliseSolo,Recomendacao 
from .serializers import UsuarioSerializer,ProdutorSerializer,PropriedadeSerializer,LaboratorioSerializer,CulturaSerializer,AnaliseSoloSerializer,RecomendacaoSerializer
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class=UsuarioSerializer
    permission_classes = [IsAuthenticated]
    
    
 
class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):# Retorna apenas os produtores do usuário logado
        return Produtor.objects.filter(usuario=self.request.user)
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user) 


class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Filtra as propriedades com base no usuário logado via a relação com Produtor
        return Propriedade.objects.filter(produtor__usuario=self.request.user)

    def perform_create(self, serializer):
        # Associa o produtor vinculado ao usuário logado automaticamente
        produtor = Produtor.objects.get(usuario=self.request.user)
        serializer.save(produtor=produtor)

    

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset=Laboratorio.objects.all()
    serializer_class=LaboratorioSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Laboratorio.objects.filter(usuario=self.request.user)


class CulturaViewSet(viewsets.ModelViewSet):
    queryset=Cultura.objects.all()
    serializer_class=CulturaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Retorna apenas as culturas do usuário logado
        return Cultura.objects.filter(usuario=self.request.user)
    
class AnaliseSoloViewSet(viewsets.ModelViewSet):
    queryset=AnaliseSolo.objects.all()
    serializer_class=AnaliseSoloSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Filtra as análises de solo com base no usuário logado via Produtor
        return AnaliseSolo.objects.filter(propriedade__produtor__usuario=self.request.user)

    def perform_create(self, serializer):
        # Associa a análise de solo à propriedade do produtor vinculado ao usuário logado
        propriedade = Propriedade.objects.filter(produtor__usuario=self.request.user).first()
        if propriedade:  # Verifica se existe alguma propriedade do usuário
            serializer.save(propriedade=propriedade)
        else:
            raise ValueError("Nenhuma propriedade encontrada para o usuário logado.")
    


class RecomendacaoViewSet(viewsets.ModelViewSet):
    queryset=Recomendacao.objects.all()
    serializer_class= RecomendacaoSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Filtra as recomendações com base no usuário logado via a relação com Propriedade
        return Recomendacao.objects.filter(analise_solo__propriedade__produtor__usuario=self.request.user)

    def perform_create(self, serializer):
        # Associa a recomendação à análise de solo do produtor vinculado ao usuário logado
        analise_solo = AnaliseSolo.objects.filter(propriedade__produtor__usuario=self.request.user).first()
        if analise_solo:  # Verifica se existe alguma análise de solo do usuário
            serializer.save(analise_solo=analise_solo)
        else:
            raise ValueError("Nenhuma análise de solo encontrada para o usuário logado.")

