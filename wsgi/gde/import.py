import csv,sys,os

project_dir= os.path.dirname(os.path.abspath(__file__))+'/gde'
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django

django.setup()

from app.models import Setor, Campus, Conarq, GrupoConarq, ClassificaArquivosIfes
data = csv.reader(open("setor.csv"),delimiter=",")

for row in data:
	if row[0] != 'ID_UNIDADE':
		campus = Campus()
		setor = Setor()
		setor.id_unidade_responsavel = row[0]
		setor.id_unidade = row[1]
		campus.nome = row[4]
		setor.sigla = row[3]
		setor.nome = row[3] + " - " + row[5]
		if Campus.objects.filter(nome=campus.nome).exists():
			campus = Campus.objects.get(nome=campus.nome)
			setor.campus = campus
			setor.save()
		else:
			campus.save()
			campus = Campus.objects.get(nome=campus.nome)
			setor.campus = campus
			setor.save()

data = csv.reader(open("codigos.csv"),delimiter=",")
for row in data:
	if row[0] != 'Classe Geral':
		conarq = Conarq()
		grupoConarq = GrupoConarq()
		classificaArquivosIfes = ClassificaArquivosIfes()
		conarq.codigo = row[1]
		conarq.assunto = row[3]
		conarq.faseCorrente = row[4]
		conarq.faseIntermediaria = row[5]
		conarq.destinacaoFinal = row[6]
		conarq.observacoes = row[7]
		grupoConarq.codigo = row[0]
		grupoConarq.nome = row[8]
		classificaArquivosIfes.codigo = row[2]
		if GrupoConarq.objects.filter(codigo=grupoConarq.codigo).exists():
			conarq.codGrupo = GrupoConarq.objects.get(codigo=grupoConarq.codigo)
			conarq.save()
			classificaArquivosIfes.conarq = conarq
		else:
			grupoConarq.save()
			conarq.codGrupo = grupoConarq
			conarq.save()
			classificaArquivosIfes.conarq = conarq
		classificaArquivosIfes.save()