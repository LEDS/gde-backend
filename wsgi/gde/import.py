import csv,sys,os

project_dir= os.path.dirname(os.path.abspath(__file__))+'/gde'
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django

django.setup()

from app.models import Setor, Campus
data = csv.reader(open("setor.csv"),delimiter=",")

for row in data:
	if row[0] != 'ID_UNIDADE':
		campus = Campus()
		setor = Setor()
		setor.id_unidade_responsavel = row[0]
		setor.id_unidade = row[1]
		campus.nome = row[3] + "-" + row[4]
		setor.sigla = row[3]
		setor.nome = row[5]
		if Campus.objects.filter(nome=campus.nome).exists():
			campus = Campus.objects.get(nome=campus.nome)
			campus = Campus.objects.get(pk=campus.id)
			setor.campus = campus
			setor.save()
		else:
			campus.save()
			campus = Campus.objects.get(nome=campus.nome)
			campus = Campus.objects.get(pk=campus.id)
			setor.campus = campus
			setor.save()