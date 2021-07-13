from django.db import models


class AbstractModel(models.Model):
    nome = models.CharField('Nome', max_length=50,  unique=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
