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
    


class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    permission_classes = [IsAuthenticated]
    

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset=Laboratorio.objects.all()
    serializer_class=LaboratorioSerializer
    permission_classes = [IsAuthenticated]
    

class CulturaViewSet(viewsets.ModelViewSet):
    queryset=Cultura.objects.all()
    serializer_class=CulturaSerializer
    permission_classes = [IsAuthenticated]


class AnaliseSoloViewSet(viewsets.ModelViewSet):
    queryset=AnaliseSolo.objects.all()
    serializer_class=AnaliseSoloSerializer
    permission_classes = [IsAuthenticated]
    


class RecomendacaoViewSet(viewsets.ModelViewSet):
    queryset=Recomendacao.objects.all()
    serializer_class= RecomendacaoSerializer
    permission_classes = [IsAuthenticated]

