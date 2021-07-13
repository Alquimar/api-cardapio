from django.contrib import admin
from estabelecimento.models import Estabelecimento


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo')
    list_filter = ('criado_em',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Estabelecimento, EstabelecimentoAdmin)
