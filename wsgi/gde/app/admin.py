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
from django.core.mail import EmailMessage
from django.conf import settings


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



class TipologiaAdmin(admin.ModelAdmin):
    list_display = ('setor','usuario',  'nome', 'identificacao', 'atividade', 'get_status', 'acao_responder')
    list_filter = ('fases', 'usuario', 'dataEnvio',  'nome', 'identificacao', 'atividade', 'especieDocumental', 'historico','finalidade', 'nome','elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna','tipoAcumulo', 'embasamentoLegal','informacaoOutrosDocumentos', 'restricaoAcesso', 'inicioAcumulo', 'fimAcumulo','quantidadeAcumulada')
    fields = [ 'setor', 'usuario', 'fases','atividade', 'producaoSetor', 'especieDocumental', 'historico','finalidade', 'nome', 'identificacao',
        'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
        ('inicioAcumulo', 'fimAcumulo') ,('quantidadeAcumulada','tipoAcumulo'), 'embasamentoLegal',
        'informacaoOutrosDocumentos', 'restricaoAcesso']

    def get_status(self, obj):
        return obj.resposta.status
    get_status.short_description = 'Status'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
               r'^(?P<id_tipologia>.+)/resposta/$',
                self.admin_site.admin_view(self.processa_resposta),
                name='processa_resposta',
            ),
            url(
               r'^(?P<id_tipologia>.+)/visualiza/$',
                self.admin_site.admin_view(self.visualiza_resposta),
                name='visualiza_resposta',
            ),

            url(
               r'^(?P<id_tipologia>.+)/editar/$',
                self.admin_site.admin_view(self.edita_resposta),
                name='edita_resposta',
            ),

            url(
               r'^(?P<pk>.+)/visualiza_resposta/$',
                self.admin_site.admin_view(self.visualizar_resposta_servidor),
                name='visualizar_resposta_servidor',
            ),

        ]
        return custom_urls + urls

    def acao_responder(self, obj):
        if hasattr(obj, 'resposta') == False:

             return format_html(

                        '<a onclick="javascript:localStorage.setItem(\'disable\', \'false\');" class="button" href="{}">Responder</a>',
                        reverse('admin:processa_resposta', args=[obj.pk]),
                    )
        else:
            if obj.resposta.status == 'salvo':
                 return format_html(

                        '<a class="button editar" href="{}">Editar</a>',
                        reverse('admin:edita_resposta', args=[obj.pk]),
                    )
            else:

                return format_html(
                '<a class="button visualizar" href="{}">Visualizar</a>',
                        reverse('admin:visualiza_resposta', args=[obj.pk]),
                    )
        
    acao_responder.short_description = 'Resposta'
    acao_responder.allow_tags = True

    def processa_resposta(self, request, id_tipologia,*args, **kwargs):
        tipologia = get_object_or_404(Tipologia, pk=id_tipologia)
        usuario = tipologia.usuario
        email_usuario = usuario.user.email
        response_data = {}
        resposta = None
        id_resposta = ''
        if request.POST:
            form_resposta = FormResposta(request.POST)
            if form_resposta.is_valid():
                
                codigo = form_resposta.cleaned_data['codigo_ifes']
                resposta = form_resposta.cleaned_data['resposta']
                observacoes = form_resposta.cleaned_data['observacoes']                
                if(request.POST.get('salvar')):
                    status = 'salvo'
                    if Resposta.objects.filter(tipologia=tipologia).exists():
                        resposta = Resposta.objects.get(tipologia=tipologia)
                        resposta.codigo_ifes = form_resposta.cleaned_data['codigo_ifes']
                        resposta.resposta = form_resposta.cleaned_data['resposta']
                        resposta.observacoes = form_resposta.cleaned_data['observacoes']
                        resposta.status = status
                        resposta.save()
                    else:
                        resposta = Resposta.objects.create(tipologia=tipologia, codigo_ifes=codigo, resposta=resposta, observacoes=observacoes, status=status)
                    fase_respondido = Fase.objects.get(nome='Aguardando Resposta')
                    tipologia.fases = fase_respondido
                    tipologia.save()
                elif(request.POST.get('enviar')):
                    status = 'enviado'
                    if Resposta.objects.filter(tipologia=tipologia).exists():
                        resposta = Resposta.objects.get(tipologia=tipologia)
                        resposta.codigo_ifes = form_resposta.cleaned_data['codigo_ifes']
                        resposta.resposta = form_resposta.cleaned_data['resposta']
                        resposta.observacoes = form_resposta.cleaned_data['observacoes']
                        resposta.status = status
                        resposta.save()
                    else:
                        resposta = Resposta.objects.create(tipologia=tipologia, codigo_ifes=codigo, resposta=resposta, observacoes=observacoes, status=status)
                    fase_respondido = Fase.objects.get(nome='Analisado')
                    tipologia.fases = fase_respondido
                    tipologia.save()
                    dominio = settings.DEFAULT_DOMAIN
                    assunto = 'Sled - Notificação de resposta '
                    corpo = 'Sua tipologia '+tipologia.nome+ ' foi respondida, para visualizar a resposta acesse:\n\n' + dominio+ '?next=/tipologia/' +str(tipologia.id)+ '/resposta' + '\n\nAtenciosamente,\nEquipe Sled.'
                    email = EmailMessage(assunto, corpo, to=[email_usuario])
                    email.send()
                self.message_user(request, status+' com sucesso!')
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
            form_resposta = FormResposta()


        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form_resposta
        context['tipologia'] = tipologia
        if resposta == None:
            context['resposta'] = None
        else:
            context['resposta'] = resposta.pk
        context['title'] = 'Cadastro de resposta'
        return TemplateResponse(
            request,
            'cadastro_resposta.html',
            context,
        )


    def visualiza_resposta(self, request, id_tipologia,*args, **kwargs):
            resposta = Resposta.objects.get(tipologia_id=id_tipologia)
            context = self.admin_site.each_context(request)
            context['opts'] = self.model._meta
            context['title'] = 'Visualizar resposta'
            context['resposta'] = resposta
            return TemplateResponse(
            request,
            'resposta_formulario_admin.html',
            context,
            )

    def visualizar_resposta_servidor(self, request, pk,*args, **kwargs):
            resposta = get_object_or_404(Resposta, pk=pk)
            context = self.admin_site.each_context(request)
            context['opts'] = self.model._meta
            context['title'] = 'Vizualizar resposta'
            context['resposta'] = resposta
            return TemplateResponse(
            request,
            'resposta_formulario_admin.html',
            context,
            )

            

    def edita_resposta(self, request, id_tipologia, *args, **kwargs):
        tipologia = get_object_or_404(Tipologia, pk=id_tipologia)
        usuario = tipologia.usuario
        email_usuario = usuario.user.email
        resposta = Resposta.objects.get(tipologia_id=id_tipologia)
        response_data = {}
        if request.POST:
            form_resposta = FormResposta(request.POST, instance=resposta)
            if form_resposta.is_valid():
                resposta = form_resposta.save(commit=False)
                if request.POST.get('salvar'):
                    status = 'salvo'
                elif request.POST.get('enviar'):
                    status = 'enviado'
                    fase_respondido = Fase.objects.get(nome='Analisado')
                    tipologia.fases = fase_respondido
                    tipologia.save()
                    dominio = settings.DEFAULT_DOMAIN
                    assunto = 'Sled - Notificação de resposta '
                    corpo = 'Sua tipologia '+tipologia.nome+ ' foi respondida, para visualizar a resposta acesse:\n\n' + dominio+ '?next=/tipologia/' +str(tipologia.id)+ '/resposta' + '\n\nAtenciosamente,\nEquipe Sled.'
                    email = EmailMessage(assunto, corpo, to=[email_usuario])
                    email.send()
                resposta.codigo_ifes = form_resposta.cleaned_data['codigo_ifes']
                resposta.resposta = form_resposta.cleaned_data['resposta']
                resposta.observacoes = form_resposta.cleaned_data['observacoes']
                resposta.status = status
                resposta.save()
                self.message_user(request, status+' com sucesso!')
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
            form_resposta = FormResposta(instance=resposta)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form_resposta
        context['resposta'] = resposta
        context['title'] = 'Editar resposta'
        return TemplateResponse(
            request,
            'edita_resposta.html',
            context,
        )

admin.site.register(Tipologia, TipologiaAdmin)

