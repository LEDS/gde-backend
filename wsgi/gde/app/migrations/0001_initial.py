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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descricao', models.TextField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificaArquivosIfes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conarq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(null=True, max_length=50)),
                ('assunto', models.CharField(null=True, max_length=150)),
                ('faseCorrente', models.CharField(null=True, max_length=150)),
                ('faseIntermediaria', models.CharField(null=True, max_length=150)),
                ('destinacaoFinal', models.CharField(null=True, max_length=150)),
                ('observacoes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieDocumental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoConarq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(null=True, max_length=50)),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('resposta', models.TextField()),
                ('observacoes', models.TextField(null=True)),
                ('status', models.CharField(null=True, max_length=100)),
                ('codigo_ifes', models.ForeignKey(related_name='codigo_ifes', to='app.ClassificaArquivosIfes')),
            ],
        ),
        migrations.CreateModel(
            name='RestricaoAcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('descricao', models.CharField(null=True, unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, max_length=200)),
                ('sigla', models.CharField(null=True, max_length=20)),
                ('id_unidade', models.IntegerField(null=True)),
                ('id_unidade_responsavel', models.IntegerField(null=True)),
                ('funcao', models.CharField(null=True, max_length=250)),
                ('historico', models.CharField(null=True, blank=True, max_length=250)),
                ('campus', models.ForeignKey(null=True, to='app.Campus', verbose_name='Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAcumulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(null=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('finalidade', models.TextField(null=True, verbose_name='Finalidade')),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('historico', models.CharField(null=True, blank=True, max_length=50, verbose_name='Histórico')),
                ('identificacao', models.CharField(max_length=50, unique=True, verbose_name='Identificação')),
                ('formaDocumental', models.BooleanField(verbose_name='Forma Documental', choices=[(True, 'Original'), (False, 'Copia')])),
                ('anexo', models.BooleanField(verbose_name='Anexo', choices=[(True, 'Sim'), (False, 'Não')])),
                ('relacaoInterna', models.BooleanField(verbose_name='Relação interna', choices=[(True, 'Sim'), (False, 'Não')])),
                ('relacaoExterna', models.BooleanField(verbose_name='Relação externa', choices=[(True, 'Sim'), (False, 'Não')])),
                ('inicioAcumulo', models.IntegerField(verbose_name='Início', choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901)])),
                ('quantidadeVias', models.BooleanField(verbose_name='Quantidade de vias', choices=[(True, 'Sim'), (False, 'Não')])),
                ('fimAcumulo', models.IntegerField(verbose_name='Fim', choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901)])),
                ('quantidadeAcumulada', models.IntegerField(verbose_name='Quantidade acumulada', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)])),
                ('embasamentoLegal', models.CharField(null=True, max_length=50, verbose_name='Embasamento legal')),
                ('informacaoOutrosDocumentos', models.BooleanField(verbose_name='Informações em outros documentos', choices=[(True, 'Sim'), (False, 'Não')])),
                ('producaoSetor', models.BooleanField(verbose_name='Produzido pelo setor', choices=[(True, 'Produzido neste setor'), (False, 'Recebido por este setor')])),
                ('dataEnvio', models.DateField(null=True, auto_now=True, verbose_name='Data de envio')),
                ('atividade', models.ForeignKey(to='app.Atividade', verbose_name='Atividade', related_name='atividade')),
                ('elemento', models.ManyToManyField(related_name='elemento', verbose_name='Elemento', to='app.Elemento')),
                ('especieDocumental', models.ForeignKey(to='app.EspecieDocumental', verbose_name='Espécie documental', related_name='especieDocumental')),
                ('fases', models.ForeignKey(to='app.Fase', verbose_name='Status', related_name='fases')),
                ('genero', models.ManyToManyField(related_name='genero', verbose_name='Gênero', to='app.Genero')),
                ('restricaoAcesso', models.ManyToManyField(related_name='restricaoAcesso', verbose_name='Restrições de acesso', to='app.RestricaoAcesso')),
                ('setor', models.ForeignKey(to='app.Setor', verbose_name='Setor', related_name='setor')),
                ('suporte', models.ForeignKey(to='app.Suporte', verbose_name='Suporte', related_name='suporte')),
                ('tipoAcumulo', models.ForeignKey(null=True, to='app.TipoAcumulo', related_name='tipoAcumulo', verbose_name='Tipo de acúmulo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('setor', models.ForeignKey(null=True, to='app.Setor', verbose_name='Setor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(to='app.Usuario', verbose_name='Usuário', related_name='usuario'),
        ),
        migrations.AddField(
            model_name='resposta',
            name='tipologia',
            field=models.OneToOneField(to='app.Tipologia', related_name='resposta'),
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
