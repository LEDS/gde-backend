# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("insert into app_fase (nome) values ('Levantamento');"),
		migrations.RunSQL("insert into app_fase (nome) values ('Aguardando Resposta');"),
		migrations.RunSQL("insert into app_fase (nome) values ('Analisado');"),
		migrations.RunSQL("insert into app_especiedocumental (nome) values ('Ata');"),
		migrations.RunSQL("insert into app_especiedocumental (nome) values ('Memorando');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Logomarca');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Numeração Sequencial');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Datas');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Numero setor destino');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Assinatura');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('Título, se: despacho, memorando, outros');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('assunto');"),
		migrations.RunSQL("insert into app_elemento (nome) values ('carimbo');"),
		migrations.RunSQL("insert into app_suporte (nome) values ('Papel');"),
		migrations.RunSQL("insert into app_suporte (nome) values ('Eletromagnético (Fita magnética)');"),
		migrations.RunSQL("insert into app_suporte (nome) values ('Eletronico (Meio Digital)');"),
		migrations.RunSQL("insert into app_suporte (nome) values ('Digitalizado');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Textual');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Imagem');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Audiovisual');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Bibliográfico');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Cartográfico');"),
		migrations.RunSQL("insert into app_genero (nome) values ('Eletrônico');"),
		migrations.RunSQL("insert into app_restricaoacesso (descricao) values ('informações relativas à intimidade, vida privada, honra e imagem das pessoas');"),
		migrations.RunSQL("insert into app_restricaoacesso (descricao) values ('informações cujo conhecimento por pessoas não autorizadas possa acarretar danos ao andamento do processo em questão');"),
		migrations.RunSQL("insert into app_restricaoacesso (descricao) values ('o documento compõe um Processo Administrativo Disciplinar');"),
		migrations.RunSQL("insert into app_restricaoacesso (descricao) values ('o documento requer sigilo fiscal, bancário, comercial, entre outros');"),
		migrations.RunSQL("insert into app_tipoacumulo (nome) values ('Caixa');"),
		migrations.RunSQL("insert into app_tipoacumulo (nome) values ('Envelope');"),
		migrations.RunSQL("insert into app_tipoacumulo (nome) values ('Pasta');"),
    ]