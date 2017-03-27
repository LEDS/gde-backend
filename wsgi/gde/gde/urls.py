"""gde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.views import *
from app import admin as adminMethod

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^register/$', cadastroUsuario),
                  url(r'^home/$', home),
                  url(r'^user/(?P<pk>[\d]+)/$', user_detail),
                  url(r'^$', auth_views.login, {'template_name': 'login.html'}),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
                  url(r'^especieDocumental/$', especieDocumental),
                  url(r'^especieDocumental/(?P<pk>\d+)/edit/$', especieDocumental_edit, name='especieDocumental_edit'),
                  url(r'^especiesDocumentais_list/$', especiesDocumentais_list),
                  url(r'^especieDocumental/(?P<pk>\d+)/remove/$', especieDocumental_remove, name='especieDocumental_remove'),
                  url(r'^setor/$', cadastrar_setor),
                  url(r'^setores_list/$', setores_list),
                  url(r'^setor/(?P<pk>\d+)/edit/$', setor_edit, name='setor_edit'),
                  url(r'^setor/(?P<pk>\d+)/remove/$', setor_remove, name='setor_remove'),
                  url(r'^campus/$', campus),
                  url(r'^campi_list/$', campi_list),
                  url(r'^campus/(?P<pk>\d+)/edit/$', campus_edit, name='campus_edit'),
                  url(r'^campus/(?P<pk>\d+)/remove/$', campus_remove, name='campus_remove'),
                  url(r'^atividade/$', atividade, name='atividade'),
                  url(r'^atividades_list/$', atividades_list, name='atividades_list'),
                  url(r'^atividade/(?P<pk>\d+)/edit/$', atividade_edit, name='atividade_edit'),
                  url(r'^atividade/(?P<pk>\d+)/remove/$', atividade_remove, name='atividade_remove'),
                  url(r'^levantamento_list/$', levantamento_list, name='levantamento_list'),
                  url(r'^levantamento/(?P<pk>\d+)/edit/$', levantamento_edit, name='levantamento_edit'),
                  url(r'^tipologia/$', cadastrar_tipologia, name="cadastrar_tipologia"),
                  url(r'^levantamento/(?P<pk>\d+)/view/$', levantamento_view, name='levantamento_view'),
                  #url(r'^processa_resposta/$', adminMethod.processa_resposta, name='processa_resposta'),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

