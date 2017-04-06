# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
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
        migrations.AlterField(
            model_name='resposta',
            name='tipologia',
            field=models.OneToOneField(related_name='resposta', to='app.Tipologia'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='nome',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='anexo',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Anexo'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='atividade',
            field=models.ForeignKey(verbose_name='Atividade', related_name='atividade', to='app.Atividade'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='dataEnvio',
            field=models.DateField(null=True, auto_now=True, verbose_name='Data de envio'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='elemento',
            field=models.ManyToManyField(verbose_name='Elemento', to='app.Elemento', related_name='elemento'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='embasamentoLegal',
            field=models.CharField(null=True, verbose_name='Embasamento legal', max_length=50),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='especieDocumental',
            field=models.ForeignKey(verbose_name='Espécie documental', related_name='especieDocumental', to='app.EspecieDocumental'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='fases',
            field=models.ForeignKey(verbose_name='Status', related_name='fases', to='app.Fase'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='fimAcumulo',
            field=models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='finalidade',
            field=models.TextField(null=True, verbose_name='Finalidade'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='formaDocumental',
            field=models.BooleanField(choices=[(True, 'Original'), (False, 'Copia')], verbose_name='Forma Documental'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='genero',
            field=models.ManyToManyField(verbose_name='Gênero', to='app.Genero', related_name='genero'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='historico',
            field=models.CharField(null=True, verbose_name='Histórico', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='identificacao',
            field=models.CharField(verbose_name='Identificação', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='informacaoOutrosDocumentos',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Informações em outros documentos'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='inicioAcumulo',
            field=models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='nome',
            field=models.CharField(verbose_name='Nome', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='producaoSetor',
            field=models.BooleanField(choices=[(True, 'Produzido neste setor'), (False, 'Recebido por este setor')], verbose_name='Produzido pelo setor'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='quantidadeAcumulada',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)], verbose_name='Quantidade acumulada', blank=True),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='quantidadeVias',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Quantidade de vias'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='relacaoExterna',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Relação externa'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='relacaoInterna',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], verbose_name='Relação interna'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='restricaoAcesso',
            field=models.ManyToManyField(verbose_name='Restrições de acesso', to='app.RestricaoAcesso', related_name='restricaoAcesso'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='setor',
            field=models.ForeignKey(verbose_name='Setor', related_name='setor', to='app.Setor'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='suporte',
            field=models.ForeignKey(verbose_name='Suporte', related_name='suporte', to='app.Suporte'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='tipoAcumulo',
            field=models.ForeignKey(verbose_name='Tipo de acúmulo', blank=True, related_name='tipoAcumulo', null=True, to='app.TipoAcumulo'),
        ),
        migrations.AlterField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(verbose_name='Usuário', related_name='usuario', to='app.Usuario'),
        ),
    ]