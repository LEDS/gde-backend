from django.contrib import admin
from .models import Setor
from .models import EspecieDocumental, Campus, Atividade,Elemento, Suporte, Genero, RestricaoAcesso, Fase, Tipologia, Usuario, TipoAcumulo, Conarq, Resposta, GrupoConarq

admin.site.register(Campus)
admin.site.register(Atividade)
admin.site.register(EspecieDocumental)
admin.site.register(Setor)
admin.site.register(TipoAcumulo)
admin.site.register(Elemento)
admin.site.register(Suporte)
admin.site.register(Genero)
admin.site.register(RestricaoAcesso)
admin.site.register(Fase)
#admin.site.register(Tipologia)
admin.site.register(Usuario)
admin.site.register(GrupoConarq)
admin.site.register(Conarq)
admin.site.register(Resposta)

from django.utils.html import format_html
from django.core.urlresolvers import reverse

# define the admin class:
class TipologiaAdmin(admin.ModelAdmin):
    list_display = ('setor','usuario',  'nome', 'identificacao', 'atividade', 'display_element' )
    list_filter = ('setor','usuario',  'nome', 'identificacao', 'atividade')
    fields = [ 'setor', 'usuario', 'atividade', 'producaoSetor', 'especieDocumental', 'historico','finalidade', 'nome', 'identificacao',
        'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
        ('inicioAcumulo', 'fimAcumulo') ,('quantidadeAcumulada','tipoAcumulo'), 'embasamentoLegal',
        'informacaoOutrosDocumentos', 'restricaoAcesso']


admin.site.register(Tipologia, TipologiaAdmin)

