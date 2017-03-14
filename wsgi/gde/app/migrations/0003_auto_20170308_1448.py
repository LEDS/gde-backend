# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tipologia_dataenvio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologia',
            name='dataEnvio',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
