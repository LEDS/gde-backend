# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificaarquivosifes',
            name='grupo',
        ),
        migrations.AddField(
            model_name='resposta',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
