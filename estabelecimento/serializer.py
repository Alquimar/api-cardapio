from rest_framework import serializers
from estabelecimento.models import Estabelecimento


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['id', 'nome', 'ativo']
