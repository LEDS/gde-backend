from django import forms
from django.forms import ModelForm, Select, TextInput, EmailInput, ChoiceField, CharField, EmailInput,RadioSelect, ModelMultipleChoiceField, SelectMultiple
from .models import *
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.widgets import HiddenInput, FileInput
from django.contrib.auth.models import User

class HTML5RequiredMixin(object):

    def __init__(self, *args, **kwargs):
        super(HTML5RequiredMixin, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'browser-default'
            if (self.fields[field].required and
               type(self.fields[field].widget) not in
                    (AdminFileWidget, HiddenInput, FileInput) and
               '__prefix__' not in self.fields[field].widget.attrs):

                    self.fields[field].widget.attrs['required'] = 'required'
                    if self.fields[field].label:
                        self.fields[field].label += ' *'

class FormAtividade(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormAtividade, self).__init__(*args,**kwargs)
        self.fields['descricao'].widget.attrs['required'] = 'required'

    class Meta:
        model = Atividade
        fields = ['descricao']
        labels = {
            'descricao':'Descreva a atividade que o seu setor exerce:'
        }


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus', 'nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'}),
             'nome': TextInput(attrs={'class':'validate'})
                    }
class FormCampus(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']


class FormTipologia(ModelForm):
    def __init__(self, *args, **kwargs):
        setor = kwargs.pop('setor', None)
        super(FormTipologia, self).__init__(*args,**kwargs)
        self.fields['atividade'] = forms.ModelChoiceField(required=True, queryset=Atividade.objects.filter(setor=setor), widget=forms.Select(), label='Este documento está relacionado a qual atividade do setor?')
        self.fields['atividade'].widget.attrs['required'] = 'required'
        self.fields['producaoSetor'].widget.attrs['required'] = 'required'
        self.fields['formaDocumental'].widget.attrs['required'] = 'required'
        self.fields['quantidadeVias'].widget.attrs['required'] = 'required'
        self.fields['anexo'].widget.attrs['required'] = 'required'
        self.fields['relacaoInterna'].widget.attrs['required'] = 'required'
        self.fields['relacaoExterna'].widget.attrs['required'] = 'required'
        self.fields['informacaoOutrosDocumentos'].widget.attrs['required'] = 'required'


    class Meta:
        model = Tipologia

        fields = [ 'atividade', 'producaoSetor', 'especieDocumental', 'historico','finalidade', 'nome', 'identificacao',
                  'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo','quantidadeAcumulada','tipoAcumulo', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso']

        labels = {
            'producaoSetor':'Este documento é:',
            'especieDocumental':'Espécie documental:',
            'identificacao':'Identificações no documento:',
            'formaDocumental':'Forma documental:',
            'elemento':'Marque os itens presentes neste documento:',
            'suporte':'Em qual suporte a informação circula?',
            'anexo':'Este documento pussui anexo?',
            'genero':'Qual o gênero predominante do documento?',
            'nome':'Nome do documento:',
            'finalidade':'Ação que gerou este documento / Objetivo para o qual foi produzido:',
            'relacaoInterna':'Este documento será encaminhado para outros setores?',
            'relacaoExterna':'Este documento será encaminhado para algum órgão externo ao Ifes?',
            'inicioAcumulo':'Qual o período de abrangência deste tipo de documento?',
            'quantidadeAcumulada':'Qual a quantidade e a forma de armazenamento deste documento?',
            'quantidadeVias':'Produz mais de uma via deste documento?',
            'embasamentoLegal':'Embasamento Legal:',
            'informacaoOutrosDocumentos':'Informações registradas em outros documentos:',
            'restricaoAcesso':'O documento contém informações que necessitam de restrição de acesso?',
            'historico':'Nome do setor presente no documento (se for diferente do nome atual do setor):',
        }

        help_texts={

            'nome':'Dica: Nome utilizado pelo setor para identificar o documento (Ex.: Folha de Ponto; Relatório de Atividades).',
            'identificacao':'Dica: Números e siglas presentes no documento (Ex.: Mem. nº 006-2016-DACV)',
            'embasamentoLegal':'Dica: Existe alguma normativa ou legislação específica sobre a configuração (Boletim, certidão, etc) que este documento possui e o conteúdo tratado nele?',
            'informacaoOutrosDocumentos':'Dica: As informações que estão neste documento encontram-se também em outros? (Ex: relatórios parciais que têm suas informações compiladas em um relatório final)',
        }

        widgets={
            'quantidadeAcumulada':Select(attrs={'onchange':'quantidadeObrigatoriaAcumulada(this)'}),
            'tipoAcumulo':Select(attrs={'onchange':'quantidadeObrigatoriaTipo(this)'}),


        }

class FormUser(ModelForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'id':'id-username'}),
            'password':TextInput(attrs={'id':'id-password', 'type':'password'}),

        }
        labels = {
            'username': ('SIAPE:'),
            'password': ('Senha:'),

        }
        help_texts={
            'username':'',
        }

class FormParcialSetor(ModelForm):
    class Meta:
        model = Setor
        exclude = ['nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'})
                    }


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['setor']
        widgets = {
            'setor': Select(attrs={'id':'id-setor','class':'browser-default selectField'}),
        }
