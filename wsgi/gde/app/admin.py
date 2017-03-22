from django.contrib import admin
from .models import Setor
from .models import EspecieDocumental, Campus, Atividade,Elemento, Suporte, Genero, RestricaoAcesso, Fase, Tipologia, Usuario, TipoAcumulo, Conarq, Resposta, GrupoConarq, ClassificaArquivosIfes
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .forms import FormResposta
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


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
admin.site.register(ClassificaArquivosIfes)


# define the admin class:
class TipologiaAdmin(admin.ModelAdmin):
    list_display = ('setor','usuario',  'nome', 'identificacao', 'atividade', 'get_status', 'acao_responder')
    list_filter = ('setor','usuario',  'nome', 'identificacao', 'atividade')
    fields = [ 'setor', 'usuario', 'atividade', 'producaoSetor', 'especieDocumental', 'historico','finalidade', 'nome', 'identificacao',
        'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
        ('inicioAcumulo', 'fimAcumulo') ,('quantidadeAcumulada','tipoAcumulo'), 'embasamentoLegal',
        'informacaoOutrosDocumentos', 'restricaoAcesso']

    def get_status(self, obj):
        return obj.resposta.status
    get_status.short_description = 'Status da resposta'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
               r'^(?P<id_tipologia>.+)/resposta/$',
                self.admin_site.admin_view(self.processa_resposta),
                name='processa_resposta',
            )
        ]
        return custom_urls + urls
    def acao_responder(self, obj):
        if obj.resposta.status == 'salvo':
            return format_html(

            '<a class="button" href="{}">Editar</a>',
            reverse('admin:processa_resposta', args=[obj.pk]),
            )

        elif obj.resposta.status == 'enviado':
            return format_html(

            '<a class="button" href="{}">Visualizar</a>',
            reverse('admin:processa_resposta', args=[obj.pk]),
            )
        else:

            return format_html(

                '<a class="button" href="{}">Resposta</a>',
                reverse('admin:processa_resposta', args=[obj.pk]),
            )

    acao_responder.short_description = 'Resposta'
    acao_responder.allow_tags = True

    def processa_resposta(self, request, id_tipologia, *args, **kwargs):
        return self.processa_acao(
            request=request,
            id=id_tipologia,
            form_acao=FormResposta,
        )

    def processa_acao(
        self,
        request,
        id,
        form_acao,
    ):
        tipologia = get_object_or_404(Tipologia, pk=id)
        response_data = {}
        if request.POST:
            form_resposta = form_acao(request.POST)
            if form_resposta.is_valid():
                if(request.POST.get('salvar')):
                    status = 'Salvo'
                elif(request.POST.get('enviar')):
                    status = 'enviado'
                codigo = form_resposta.cleaned_data['codigo_ifes']
                resposta = form_resposta.cleaned_data['resposta']
                observacoes = form_resposta.cleaned_data['observacoes']
                Resposta.objects.create(tipologia=tipologia, codigo_ifes=codigo, resposta=resposta, observacoes=observacoes, status=status)
                self.message_user(request, 'Success')
            else:
                self.message_user(request, 'Error'+form_resposta)
        else:
            if request.GET.get('codigo'):
                codigo = request.GET.get('codigo')
                classe_ifes = ClassificaArquivosIfes.objects.get(codigo=codigo)
                conarq = Conarq.objects.get(pk = classe_ifes.conarq.pk)
                grupo_conarq = GrupoConarq.objects.get(pk=conarq.codGrupo.pk)
                response_data['classe'] = grupo_conarq.codigo
                response_data['nome_classe'] = grupo_conarq.nome
                response_data['subclasse'] = conarq.codigo
                response_data['assunto'] = conarq.assunto
                response_data['fase_corrente'] = conarq.faseCorrente
                response_data['fase_intermediaria'] = conarq.faseIntermediaria
                response_data['destinacao_final'] = conarq.destinacaoFinal
                response_data['observacoes'] = conarq.observacoes

                return JsonResponse(response_data)
            form_resposta = form_acao()


        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form_resposta
        context['tipologia'] = tipologia
        context['title'] = 'Cadastro de resposta'
        return TemplateResponse(
            request,
            'cadastro_resposta.html',
            context,
        )

admin.site.register(Tipologia, TipologiaAdmin)

