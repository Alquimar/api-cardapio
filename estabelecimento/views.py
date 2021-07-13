from rest_framework import viewsets
from estabelecimento.models import Estabelecimento
from estabelecimento.serializer import EstabelecimentoSerializer


class EstabelecimentosViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
