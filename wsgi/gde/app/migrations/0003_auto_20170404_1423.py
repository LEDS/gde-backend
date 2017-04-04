# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170328_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='setor',
            name='historico',
        ),
        migrations.AddField(
            model_name='setor',
            name='id_unidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='setor',
            name='id_unidade_responsavel',
            field=models.IntegerField(null=True),
        ),
    ]
