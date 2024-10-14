
from rest_framework import serializers
from .models import Usuario, Produtor, Propriedade, Laboratorio, Cultura, AnaliseSolo, Recomendacao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'
# Associa automaticamente o usuário logado durante a criação
    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
# Associa automaticamente o usuário logado durante a atualização
    def update(self, instance, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().update(instance, validated_data)

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'
# Associa automaticamente o usuário logado durante a criação
    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
# Associa automaticamente o usuário logado durante a atualização
    def update(self, instance, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().update(instance, validated_data)

class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'
# Associa automaticamente o usuário logado durante a criação
    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
# Associa automaticamente o usuário logado durante a atualização
    def update(self, instance, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().update(instance, validated_data)

class AnaliseSoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseSolo
        fields = '__all__'

class RecomendacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacao
        fields = '__all__'