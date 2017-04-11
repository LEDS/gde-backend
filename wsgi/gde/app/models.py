from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

def gera_anos(anoInicial):
    YEAR_CHOICES = []
    for r in range((datetime.datetime.now().year), anoInicial, -1):
        YEAR_CHOICES.append((r,r))
    return YEAR_CHOICES

def gera_inteiros_positivos(quantidade):
    inteiros_positivos = []
    for r in range(1, quantidade):
        inteiros_positivos.append((r, r))
    return inteiros_positivos

def gera_sim_nao():
    saida = [(True, 'Sim'), (False, 'Não')]
    return saida

class EspecieDocumental(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=500, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    campus = models.ForeignKey(Campus, null=True, blank=False, verbose_name='Campus')
    nome = models.CharField(max_length=200, null=True, blank=False, unique=False)
    sigla = models.CharField(max_length=20, null=True, blank=False, unique=False)
    id_unidade = models.IntegerField(null=True, blank=False)
    id_unidade_responsavel = models.IntegerField(null=True, blank=False)
    funcao = models.CharField(max_length=250, null=True, blank=False, unique=False)
    historico = models.CharField(max_length=250, null=True, blank=True, unique=False)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    setor = models.ForeignKey(Setor, null=True, blank=False)
    descricao = models.TextField(null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, null=True, blank=False, verbose_name='Setor')

    def __str__(self):
        return self.user.first_name

class Elemento(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Suporte(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome

class RestricaoAcesso(models.Model):
    descricao = models.CharField(max_length=200, null=True, blank=False, unique=True)

    def __str__(self):
        return self.descricao

class Fase(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=False, unique=True)

    def __str__(self):
        return self.nome


class TipoAcumulo(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=False, unique=False)
    def __str__(self):
        return self.nome

class Tipologia(models.Model):
    atividade = models.ForeignKey(Atividade, related_name='atividade', verbose_name='Atividade')
    setor = models.ForeignKey(Setor, related_name='setor', verbose_name='Setor')
    usuario = models.ForeignKey(Usuario, related_name='usuario', verbose_name='Usuário')
    fases = models.ForeignKey(Fase, related_name='fases', verbose_name='Status')
    especieDocumental = models.ForeignKey(EspecieDocumental,related_name='especieDocumental', verbose_name='Espécie documental')
    finalidade = models.TextField('Finalidade', null=True, blank=False, unique=False)
    nome = models.CharField('Nome', max_length=50, blank=False, unique=True)
    historico = models.CharField('Histórico', max_length=50,null=True, blank=True)
    identificacao = models.CharField('Identificação', max_length=50, blank=False, unique=True)
    elemento = models.ManyToManyField(Elemento, related_name='elemento', verbose_name='Elemento')
    suporte = models.ForeignKey(Suporte, related_name='suporte', verbose_name='Suporte')
    formaDocumental = models.BooleanField('Forma Documental', choices=((True, 'Original'), (False, 'Copia')), blank=False)
    genero = models.ManyToManyField(Genero, related_name='genero', verbose_name='Gênero')
    anexo = models.BooleanField('Anexo', choices=gera_sim_nao(), blank=False)
    relacaoInterna = models.BooleanField('Relação interna', choices=gera_sim_nao(), blank=False)
    relacaoExterna = models.BooleanField('Relação externa', choices=gera_sim_nao(), blank=False)
    inicioAcumulo = models.IntegerField('Início', choices=gera_anos(1900), blank=False)
    quantidadeVias = models.BooleanField('Quantidade de vias', choices=gera_sim_nao(), blank=False)
    fimAcumulo = models.IntegerField('Fim', choices=gera_anos(1900), blank=False)
    quantidadeAcumulada = models.IntegerField('Quantidade acumulada', choices=gera_inteiros_positivos(100),blank=True)
    tipoAcumulo = models.ForeignKey(TipoAcumulo, related_name='tipoAcumulo', blank=True, null=True, verbose_name='Tipo de acúmulo')
    embasamentoLegal = models.CharField('Embasamento legal', max_length=50, null=True, blank=False, unique=False)
    informacaoOutrosDocumentos = models.BooleanField('Informações em outros documentos', choices=gera_sim_nao(), blank=False)
    restricaoAcesso = models.ManyToManyField(RestricaoAcesso, related_name='restricaoAcesso', verbose_name='Restrições de acesso')
    producaoSetor = models.BooleanField('Produzido pelo setor', choices=((True, 'Produzido neste setor'), (False, 'Recebido por este setor')),blank=False)
    dataEnvio = models.DateField('Data de envio', auto_now=True, null=True)

    def __str__(self):
        return 'setor:'+self.setor.nome+'usuário:'+self.usuario.user.username+'espécie:'+\
               self.especieDocumental.nome+'nome:'+self.nome


class GrupoConarq(models.Model):
    codigo = models.CharField(max_length=50,blank=False,null=True)
    nome = models.CharField(blank=False,max_length=150)

    def __str__(self):
        return self.nome

class Conarq(models.Model):
    codGrupo = models.ForeignKey(GrupoConarq,related_name="codGrupo",blank=False)
    codigo = models.CharField(max_length=50,blank=False,null=True)
    assunto = models.CharField(max_length=150,blank=False,null=True)
    faseCorrente = models.CharField(max_length=150,blank=False,null=True)
    faseIntermediaria = models.CharField(max_length=150,blank=False,null=True)
    destinacaoFinal = models.CharField(max_length=150,blank=False,null=True)
    observacoes = models.TextField(blank=False,null =True)
    def __str__(self):
        return self.assunto

class ClassificaArquivosIfes(models.Model):
    codigo = models.CharField(max_length=50,blank=False,null=True)
    conarq = models.ForeignKey(Conarq, related_name="conarq", blank=False)

    def __str__(self):
        return self.codigo

class Resposta(models.Model):
    tipologia = models.OneToOneField(Tipologia, related_name="resposta", on_delete=models.CASCADE, blank=False)
    codigo_ifes = models.ForeignKey(ClassificaArquivosIfes,related_name="codigo_ifes",blank=False)
    resposta = models.TextField(blank=False)
    observacoes = models.TextField(null=True)
    status = models.CharField(max_length=100,blank=False,null=True)




    def __str__(self):
        return self.resposta


