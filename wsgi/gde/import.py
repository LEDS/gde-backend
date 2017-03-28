import csv,sys,os

project_dir="/home/lucas/LEDs/gdeSSH/wsgi/gde/gde/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django

django.setup()

from app.models import Setor, Campus

data = csv.reader(open("/home/lucas/LEDs/gdeSSH/setores.csv"),delimiter=",")

for row in data:
	if row[0] != 'ID_UNIDADE':
		setor = Setor()
		campus = Campus.objects.get(pk=1)
		setor.campus = campus
		setor.nome = row[2]
		setor.save()
