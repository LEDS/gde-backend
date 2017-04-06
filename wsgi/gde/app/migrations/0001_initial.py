# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descricao', models.TextField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificaArquivosIfes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conarq',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(max_length=50, null=True)),
                ('assunto', models.CharField(max_length=150, null=True)),
                ('faseCorrente', models.CharField(max_length=150, null=True)),
                ('faseIntermediaria', models.CharField(max_length=150, null=True)),
                ('destinacaoFinal', models.CharField(max_length=150, null=True)),
                ('observacoes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=60, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieDocumental',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=60, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoConarq',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(max_length=50, null=True)),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('resposta', models.TextField()),
                ('observacoes', models.TextField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('codigo_ifes', models.ForeignKey(related_name='codigo_ifes', to='app.ClassificaArquivosIfes')),
            ],
        ),
        migrations.CreateModel(
            name='RestricaoAcesso',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('descricao', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=200, null=True)),
                ('sigla', models.CharField(max_length=20, null=True)),
                ('id_unidade', models.IntegerField(null=True)),
                ('id_unidade_responsavel', models.IntegerField(null=True)),
                ('funcao', models.CharField(max_length=250, null=True)),
                ('historico', models.CharField(max_length=250, null=True, blank=True)),
                ('campus', models.ForeignKey(to='app.Campus', verbose_name='Campus', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=60, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAcumulo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('finalidade', models.TextField(null=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('historico', models.CharField(max_length=50, null=True, blank=True)),
                ('identificacao', models.CharField(max_length=50, unique=True)),
                ('formaDocumental', models.BooleanField(choices=[(True, 'Original'), (False, 'Copia')])),
                ('anexo', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('relacaoInterna', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('relacaoExterna', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('inicioAcumulo', models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)])),
                ('quantidadeVias', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('fimAcumulo', models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)])),
                ('quantidadeAcumulada', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)], blank=True)),
                ('embasamentoLegal', models.CharField(max_length=50, null=True)),
                ('informacaoOutrosDocumentos', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('producaoSetor', models.BooleanField(choices=[(True, 'Produzido neste setor'), (False, 'Recebido por este setor')])),
                ('dataEnvio', models.DateField(null=True, auto_now=True)),
                ('atividade', models.ForeignKey(related_name='atividade', to='app.Atividade')),
                ('elemento', models.ManyToManyField(related_name='elemento', to='app.Elemento')),
                ('especieDocumental', models.ForeignKey(related_name='especieDocumental', to='app.EspecieDocumental')),
                ('fases', models.ForeignKey(related_name='fases', to='app.Fase')),
                ('genero', models.ManyToManyField(related_name='genero', to='app.Genero')),
                ('restricaoAcesso', models.ManyToManyField(related_name='restricaoAcesso', to='app.RestricaoAcesso')),
                ('setor', models.ForeignKey(related_name='setor', to='app.Setor')),
                ('suporte', models.ForeignKey(related_name='suporte', to='app.Suporte')),
                ('tipoAcumulo', models.ForeignKey(related_name='tipoAcumulo', blank=True, null=True, to='app.TipoAcumulo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('setor', models.ForeignKey(to='app.Setor', verbose_name='Setor', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='tipologia',
            field=models.OneToOneField(to='app.Tipologia'),
        ),
        migrations.AddField(
            model_name='conarq',
            name='codGrupo',
            field=models.ForeignKey(related_name='codGrupo', to='app.GrupoConarq'),
        ),
        migrations.AddField(
            model_name='classificaarquivosifes',
            name='conarq',
            field=models.ForeignKey(related_name='conarq', to='app.Conarq'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='setor',
            field=models.ForeignKey(null=True, to='app.Setor'),
        ),
    ]
