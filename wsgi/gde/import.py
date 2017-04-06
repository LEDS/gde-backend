import csv,sys,os

project_dir= os.path.dirname(os.path.abspath(__file__))+'/gde'
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django

django.setup()

from app.models import Setor, Campus
data = csv.reader(open("setor.csv"),delimiter=",")

# campus = Campus()
# setor = Setor()
# campus.nome = "Serra"
# campus = Campus.objects.all()
# setor.campus = Campus.objects.get(pk=campus[0].id)
# setor.nome = "Biblioteca"
# setor.save()

for row in data:
	if row[0] != 'ID_UNIDADE':
		campus = Campus()
		setor = Setor()
		setor.nome = row[5]
		setor.id_unidade_responsavel = row[0]
		setor.id_unidade = row[1]
		setor.sigla = row[3]
		campus.nome = row[4]
		if Campus.objects.filter(nome=campus.nome).exists():
			# campus = Campus.objects.get(nome=campus.nome)
			# print(campus.id)
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

		# setor = Setor()
		# campus = Campus.objects.get(pk=1)
		# setor.campus = campus
		# setor.nome = row[2]
		# setor.save()
