import csv,sys,os

project_dir= os.path.dirname(os.path.abspath(__file__))+'/gde'
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django

django.setup()

from app.models import Conarq, GrupoConarq, ClassificaArquivosIfes
data = csv.reader(open("codigos.csv"),delimiter=",")

for row in data:
	if row[0] != 'Classe_Geral_grupo_conarq':
		conarq = Campus()
		grupoConarq = Setor()
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
		if grupoConarq.objects.filter(codigo=grupoConarq.codigo).exists():
			grupoConarq = Campus.objects.get(nome=grupoConarq.nome)
			grupoConarq = Campus.objects.get(pk=grupoConarq.id)
			setor.campus = campus
			setor.save()
		else:
			campus.save()
			campus = Campus.objects.get(nome=campus.nome)
			campus = Campus.objects.get(pk=campus.id)
			setor.campus = campus
			setor.save()