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
    setor_campus = dict()
    for (campus,setor) in [(setor.campus.id,setor.id) for setor in setores]:
            setor_campus[setor] = campus
    setor_campus_json = json.dumps(setor_campus)
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
            setor_campus = Setor.objects.get(nome=setor, campus=campus)
            Usuario.objects.create(user=user, setor=setor_campus)
            return HttpResponseRedirect(request.POST.get('next'))

    # if a GET (or any other method) we'll create a blank form
    else:
        formUser = FormUser()
        formUsuario = FormUsuario()
        formParcialSetor = FormParcialSetor()

    return render(request, 'cadastroUsuario.html', {'formParcialSetor':formParcialSetor, 'formUser': formUser, 'formUsuario':formUsuario, 'setorCampus':setor_campus_json})

@csrf_protect
@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    usuario = get_object_or_404(Usuario, pk=Usuario.objects.get(user=user).id)
    setor = get_object_or_404(Setor,  pk=usuario.setor.id)

    setores = Setor.objects.all()
    setor_campus = dict()
    for (campus__,setor__) in [(setor.campus.id,setor.id) for setor in setores]:
            setor_campus[setor__] = campus__
    setor_campus_json = json.dumps(setor_campus)

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
    return render(request, 'editarUsuario.html', {'formParcialSetor':formParcialSetor, 'formUser': formUser, 'formUsuario':formUsuario,'setorCampus':setor_campus_json})

@csrf_protect
@login_required
def home(request):
    return render(request, 'home.html')

@csrf_protect
@login_required
def especieDocumental(request):
    if request.POST:
        nome = request.POST.get('nome', None)
        existeNoBanco = EspecieDocumental.objects.filter(nome=nome).exists()
        if (nome != ''):
            if (existeNoBanco == True):
                messages.add_message(request, messages.ERROR,
                                     'A Especie Documental ja existe. Por favor, tente novamente!')
            else:
                EspecieDocumental.objects.create(nome=nome)
                return HttpResponseRedirect(request.POST.get('next'))
    return render(request, 'especieDocumental.html', {})


@csrf_protect
@login_required
def especiesDocumentais_list(request):
    especiesDocumentais = EspecieDocumental.objects.all
    return render(request, 'especiesDocumentais_list.html', {'especiesDocumentais': especiesDocumentais})


@csrf_protect
@login_required
def especieDocumental_remove(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    especieDocumental.delete()
    return redirect('app.views.especiesDocumentais_list')


@csrf_protect
@login_required
def especieDocumental_edit(request, pk):
    especieDocumental = get_object_or_404(EspecieDocumental, pk=pk)
    if request.POST:
        nome = request.POST.get('nome', None)
        existeNoBanco = EspecieDocumental.objects.filter(nome=nome).exists()
        if (nome != ''):
            if (existeNoBanco == True):
                messages.add_message(request, messages.ERROR,
                                     'A Especie Documental ja existe. Por favor, tente novamente!')
            else:
                nome = request.POST.get('nome', None)
                especieDocumental.nome = nome
                especieDocumental.save()
                return HttpResponseRedirect(request.POST.get('next'))

    return render(request, 'editarEspecieDocumental.html', {'especieDocumental': especieDocumental})

@csrf_protect
@login_required
def atividades_list(request):
    atividades = Atividade.objects.order_by('setor')
    return render(request, 'atividades_list.html', {'atividades': atividades})

@csrf_protect
@login_required()
def atividade(request):
    if request.method == 'POST':
        form = FormAtividade(request.POST)
        if form.is_valid():
            setor = form.cleaned_data['setor']
            descricao = form.cleaned_data['descricao']
            Atividade.objects.create(setor=setor,descricao=descricao)
            return HttpResponseRedirect('/atividades_list/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormAtividade()

    return render(request, 'atividade.html', {'form': form})

@csrf_protect
@login_required
def atividade_edit(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    if request.POST:
        form = FormAtividade(request.POST, instance=atividade)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.setor = form.cleaned_data['setor']
            atividade.descricao = form.cleaned_data['descricao']
            atividade.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormAtividade(instance=atividade)
    return render(request, 'editar_atividade.html', {'form': form, 'atividade': atividade})

@csrf_protect
@login_required
def atividade_remove(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    atividade.delete()
    return redirect('app.views.atividades_list')

@csrf_protect
@login_required
def setores_list(request):
    setores = Setor.objects.all
    return render(request, 'setores_list.html', {'setores': setores})


@csrf_protect
@login_required()
def cadastrar_setor(request):
    if request.method == 'POST':
        form = FormSetor(request.POST)
        if form.is_valid():
            campus = form.cleaned_data['campus']
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            funcao = form.cleaned_data['funcao']
            historico = form.cleaned_data['historico']
            Setor.objects.create(nome=nome, sigla=sigla, funcao=funcao, historico=historico, campus=campus)
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormSetor()

    return render(request, 'cadastro_setor.html', {'form': form})


@csrf_protect
@login_required
def setor_edit(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.POST:
        form = FormSetor(request.POST, instance=setor)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.campus = form.cleaned_data['campus']
            setor.nome = form.cleaned_data['nome']
            setor.sigla = form.cleaned_data['sigla']
            setor.funcao = form.cleaned_data['funcao']
            setor.historico = form.cleaned_data['historico']
            setor.save()
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormSetor(instance=setor)
    return render(request, 'editar_setor.html', {'form': form, 'setor': setor})


@csrf_protect
@login_required
def setor_remove(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    setor.delete()
    return redirect('app.views.setores_list')


@csrf_protect
@login_required
def campus(request):
    if request.method == 'POST':
        form = FormCampus(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            Campus.objects.create(nome=nome)
            return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormCampus()
    return render(request, 'campus.html', {'form': form})


@csrf_protect
@login_required
def campi_list(request):
    campi = Campus.objects.all
    return render(request, 'campi_list.html', {'campi': campi})


@csrf_protect
@login_required
def campus_edit(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    if request.POST:
        form = FormCampus(request.POST, instance=campus)
        if form.is_valid():
            campus = form.save(commit=False)
            if(Campus.objects.filter(nome=form.cleaned_data['nome'])):
                form.add_error('nome', 'Campus com este Nome já existe.')
            else:
                campus.nome = form.cleaned_data['nome']
                campus.save()
                return HttpResponseRedirect(request.POST.get('next'))
    else:
        form = FormCampus(instance=campus)
    return render(request, 'editarCampus.html', {'form': form, 'campus': campus})

@csrf_protect
@login_required
def campus_remove(request, pk):
    campus = get_object_or_404(Campus, pk=pk)
    campus.delete()
    return redirect('app.views.campi_list')

@csrf_protect

@login_required
def levantamento_list(request):
    tipologias = Tipologia.objects.all
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

@login_required
def resposta_view(request, pk):
    resposta = get_object_or_404(Resposta, pk=pk)
    return render(request, 'resposta_formulario.html',{'resposta':resposta})

@login_required()
def cadastrar_tipologia(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    setor = usuario.setor
    response_data = {}
    if request.POST:
        formAtividade = FormAtividade(request.POST)
        form = FormTipologia(request.POST, setor=setor)
        #form.errors['atividade'] = None
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
            if request.POST.get('submit_enviar') == "0":
                fase = Fase.objects.get(nome='Aguardando Resposta')
            elif request.POST.get('submit_salvar') == "1":
                fase = Fase.objects.get(nome='Levantamento')
            if form.is_valid():
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

