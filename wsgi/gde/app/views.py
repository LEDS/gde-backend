from app.models import EspecieDocumental, Setor, Campus, Atividade, Usuario, Tipologia, Fase, Resposta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from .forms import FormAtividade, FormSetor, FormCampus, FormUsuario, FormUser, FormParcialSetor
from .forms import FormAtividade, FormSetor, FormCampus, FormTipologia
from django.views.generic.list import ListView
from django.utils import timezone
import json
import logging
from django.http import JsonResponse



@csrf_protect
def cadastroUsuario(request):
    setores = Setor.objects.all()
    campi = Campus.objects.all()
    setor_campus = dict()
    setores_no_campus = dict()
    informacoes_setores_campus = dict()
    setor_campus_json = ''
    
    
    for campus in campi:
        setores_id = []
        setores_nome = []
        campus_json =dict()
        for setor in setores:
            if setor.campus.id == campus.id:
                setores_id.append(setor.id)
                setores_nome.append(setor.nome)    
        campus_json['setores_id'] = setores_id
        campus_json['setores_nome'] = setores_nome

        setores_no_campus[campus.id] = campus_json

    setor_campus_json = json.dumps(setores_no_campus)

    if request.method == 'POST':
        formUser = FormUser(request.POST)
        formParcialSetor = FormParcialSetor(request.POST)
        formUsuario = FormUsuario(request.POST)
        if formUser.is_valid() and formParcialSetor.is_valid() and formUsuario.is_valid():
            nome = formUser.cleaned_data['first_name']
            sobrenome = formUser.cleaned_data['last_name']
            siape = formUser.cleaned_data['username']
            email = formUser.cleaned_data['email']
            senha = formUser.cleaned_data['password']
            campus = formParcialSetor.cleaned_data['campus']
            setor = formUsuario.cleaned_data['setor']
            user = User.objects.create_user(siape, email, senha)
            user.last_name=sobrenome
            user.first_name=nome
            user.save()
            setor_campus = Setor.objects.get(pk=setor.pk, campus=campus)
            Usuario.objects.create(user=user, setor=setor_campus)
            return HttpResponseRedirect(request.POST.get('next'))

    # if a GET (or any other method) we'll create a blank form
    else:
        formUser = FormUser()
        formUsuario = FormUsuario()
        formParcialSetor = FormParcialSetor()

    return render(request, 'cadastroUsuario.html', {'formParcialSetor':formParcialSetor, 'formUser': formUser, 'formUsuario':formUsuario, 'setorCampus':setor_campus_json} )

@csrf_protect
@login_required
def user_detail(request, pk):

    user = get_object_or_404(User, pk=pk)
    usuario = get_object_or_404(Usuario, pk=Usuario.objects.get(user=user).id)
    setor = get_object_or_404(Setor,  pk=usuario.setor.id)

    setores = Setor.objects.all()
    campi = Campus.objects.all()
    setor_campus = dict()
    setores_no_campus = dict()
    informacoes_setores_campus = dict()
    setor_campus_json = ''
    
    
    for campus in campi:
        setores_id = []
        setores_nome = []
        campus_json =dict()
        for setor in setores:
            if setor.campus.id == campus.id:
                setores_id.append(setor.id)
                setores_nome.append(setor.nome)    
        campus_json['setores_id'] = setores_id
        campus_json['setores_nome'] = setores_nome

        setores_no_campus[campus.id] = campus_json

    setor_campus_json = json.dumps(setores_no_campus)


    if request.POST:
        formUser = FormUser(request.POST, instance=user)
        formUsuario = FormUsuario(request.POST, instance=usuario)
        formParcialSetor = FormParcialSetor(request.POST, instance=setor)
        if formUser.is_valid() and formParcialSetor.is_valid() and formUsuario.is_valid():
            user = formUser.save(commit=False)
            campus = formParcialSetor.save(commit=False)
            usuario = formUsuario.save(commit=False)
            user.first_name = formUser.cleaned_data['first_name']
            user.last_name = formUser.cleaned_data['last_name']
            user.username = formUser.cleaned_data['username']
            user.email = formUser.cleaned_data['email']
            senha = formUser.cleaned_data['password']
            if not check_password(senha, user.password):
                user.password = make_password(senha)
            user.save()
            campus_entrada = formParcialSetor.cleaned_data['campus']
            setor = formUsuario.cleaned_data['setor']
            setor_do_campus = Setor.objects.get(nome=setor, campus=campus_entrada)
            usuario.setor = setor_do_campus
            usuario.save()
            messages.success(request, 'Os dados foram atualizados com sucesso.')
    else:
        user.password = ""
        formUser = FormUser(instance=user)
        formParcialSetor = FormParcialSetor(instance=setor)
        formUsuario = FormUsuario(instance=usuario)
    return render(request, 'editarUsuario.html', {'formParcialSetor':formParcialSetor, 'formUser': formUser, 'formUsuario':formUsuario, 'setorCampus':setor_campus_json})

@csrf_protect
@login_required
def home(request):
    return render(request, 'home.html')


@csrf_protect
@login_required
def levantamento_list(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    tipologias = Tipologia.objects.all().filter(usuario=usuario)
    return render(request, 'meus_levantamentos.html', {'tipologias': tipologias})


@csrf_protect
@login_required
def levantamento_edit(request, pk):
    tipologia = get_object_or_404(Tipologia, pk=pk)
    user = request.user
    usuario = Usuario.objects.get(user=user)
    setor = usuario.setor
    if request.POST:
        form = FormTipologia(request.POST, instance=tipologia, setor=setor)
        if form.is_valid():
            tipologia = form.save(commit=False)
            if request.POST.get('submit_enviar') == "0":
                tipologia.fases = Fase.objects.get(nome='Aguardando Resposta')
            elif request.POST.get('submit_salvar') == "1":
                tipologia.fases = Fase.objects.get(nome='Levantamento')
            tipologia.especieDocumental = form.cleaned_data['especieDocumental']
            tipologia.finalidade = form.cleaned_data['finalidade']
            tipologia.nome = form.cleaned_data['nome']
            tipologia.identificacao = form.cleaned_data['identificacao']
            tipologia.atividade = form.cleaned_data['atividade']
            tipologia.elemento = form.cleaned_data['elemento']
            tipologia.suporte = form.cleaned_data['suporte']
            tipologia.formaDocumental = form.cleaned_data['formaDocumental']
            tipologia.genero = form.cleaned_data['genero']
            tipologia.anexo = form.cleaned_data['anexo']
            tipologia.relacaoInterna = form.cleaned_data['relacaoInterna']
            tipologia.relacaoExterna = form.cleaned_data['relacaoExterna']
            tipologia.inicioAcumulo = form.cleaned_data['inicioAcumulo']
            tipologia.fimAcumulo = form.cleaned_data['fimAcumulo']
            tipologia.quantidadeAcumulada = form.cleaned_data['quantidadeAcumulada']
            tipologia.tipoAcumulo = form.cleaned_data['tipoAcumulo']
            tipologia.embasamentoLegal = form.cleaned_data['embasamentoLegal']
            tipologia.informacaoOutrosDocumentos = form.cleaned_data['informacaoOutrosDocumentos']
            tipologia.restricaoAcesso = form.cleaned_data['restricaoAcesso']
            tipologia.quantidadeVias = form.cleaned_data['quantidadeVias']
            tipologia.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormTipologia(instance=tipologia, setor=setor)
    return render(request, 'editar_levantamento.html', {'form': form, 'tipologia': tipologia})

@login_required
def levantamento_view(request, pk):
    tipologia = get_object_or_404(Tipologia, pk=pk)
    return render(request, 'visualizar_levantamento.html',{'tipologia':tipologia})

def resposta_view(request, pk):
    resposta = Resposta.objects.get(tipologia=pk)
    return render(request, 'resposta_formulario.html',{'resposta':resposta})

@csrf_protect
@login_required
def cadastrar_tipologia(request):
    user = request.user
    usuario = Usuario.objects.get(user=user.pk)
    setor = usuario.setor
    response_data = {}
    if request.POST:
        formAtividade = FormAtividade(request.POST)
        form = FormTipologia(request.POST, setor=setor)
        if request.POST.get('botao_cadastrar') == "3":
            if formAtividade.is_bound and formAtividade.is_valid():
                descricao = formAtividade.cleaned_data['descricao']
                Atividade.objects.create(setor=setor,descricao=descricao)
                response_data['resposta'] = Atividade.objects.get(descricao=descricao).id
                response_data['nome_atividade'] = descricao
                return JsonResponse(response_data)
            response_data['resposta'] = '0'
            return JsonResponse(response_data)
        else:
            if form.is_valid():
                if request.POST.get('valor') == "0":
                    fase = Fase.objects.get(nome='Aguardando Resposta')
                elif request.POST.get('valor') == "1":
                    fase = Fase.objects.get(nome='Levantamento')
                especieDocumental = form.cleaned_data['especieDocumental']
                finalidade = form.cleaned_data['finalidade']
                nome = form.cleaned_data['nome']
                identificacao = form.cleaned_data['identificacao']
                atividade = form.cleaned_data['atividade']
                elementos = form.cleaned_data['elemento']
                suporte = form.cleaned_data['suporte']
                formaDocumental = form.cleaned_data['formaDocumental']
                generos = form.cleaned_data['genero']
                anexo = form.cleaned_data['anexo']
                relacaoInterna = form.cleaned_data['relacaoInterna']
                relacaoExterna = form.cleaned_data['relacaoExterna']
                inicioAcumulo = form.cleaned_data['inicioAcumulo']
                fimAcumulo = form.cleaned_data['fimAcumulo']
                quantidadeAcumulada = form.cleaned_data['quantidadeAcumulada']
                tipoAcumulo = form.cleaned_data['tipoAcumulo']
                embasamentoLegal = form.cleaned_data['embasamentoLegal']
                informacaoOutrosDocumentos = form.cleaned_data['informacaoOutrosDocumentos']
                restricoesAcesso = form.cleaned_data['restricaoAcesso']
                quantidadeVias = form.cleaned_data['quantidadeVias']
                producaoSetor = form.cleaned_data['producaoSetor']
                tipologia = Tipologia.objects.create(producaoSetor = producaoSetor, setor = setor, usuario = usuario, fases = fase, especieDocumental = especieDocumental, finalidade = finalidade, nome = nome, identificacao = identificacao, atividade = atividade, suporte = suporte, formaDocumental = formaDocumental, anexo = anexo, relacaoInterna = relacaoInterna, relacaoExterna = relacaoExterna, inicioAcumulo = inicioAcumulo, fimAcumulo = fimAcumulo, quantidadeAcumulada = quantidadeAcumulada, embasamentoLegal = embasamentoLegal, informacaoOutrosDocumentos = informacaoOutrosDocumentos, quantidadeVias = quantidadeVias, tipoAcumulo = tipoAcumulo)
                tipologia.elemento = elementos
                tipologia.genero = generos
                tipologia.restricaoAcesso = restricoesAcesso
                tipologia.save()
                return HttpResponseRedirect(request.POST.get('next'))
        
    else:
        form = FormTipologia(setor=setor)
        formAtividade = FormAtividade()

    return render(request, 'cadastro_tipologia.html', {'form': form, 'formAtividade':formAtividade})
