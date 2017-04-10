from behave import given, when, then
from app.models import Setor,Campus
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
from test.factories.campus import CampusFactory


#Scenario: Campos Vazios
@given('Estou na pagina de cadastro de um setor')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/setor')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/setor/')

@when('Submeto o cadastro de um novo setor deixando algum campo em branco')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@then('Nao conseguirei cadastrar o setor ate que eu preencha o campo nome.')
def step_impl(context):
    br = context.browser
    br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_name('nome').text == ""





#Scenario: Cadastrar novo setor
@when('Informo um campus, nome, sigla, funcao e historico')
def step_impl(context):
    br = context.browser
    
    campus = CampusFactory(nome='Serra')
    campus.save()
    campus = Campus.objects.filter(nome = 'Serra').exists()
    assert campus == True

    #select = Select(br.find_element_by_id('id_campus'))
    #select.select_by_value('1')

    br.get_screenshot_as_file('/tmp/screenshot.png')

    br.find_element_by_name('nome').send_keys('setorTeste')
    br.find_element_by_name('submit').click()
    
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()


@when('Não existir setor com mesmo nome e sigla já cadastrado para o campus escolhido')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    
    setor = Setor.objects.filter(nome = 'setorTeste', sigla = 'ST').exists()
    assert setor == False

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@when('Submeto o cadastro de um novo setor')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@then('Sou redirecionado para a pagina principal de setor')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_name('nome').text == ""

@then('O setor devera estar devidamente cadastrado.')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/setor/')
    assert br.find_element_by_name('nome').text == ""

@when('Informo um setor ja cadastrado no sistema')
def step_impl(context):
    pass
    # br = context.browser
   
    # br.find_element_by_name('nome').send_keys('setorTeste')
    # br.find_element_by_name('sigla').send_keys('ST')
    # br.find_element_by_name('funcao').send_keys('funcao')
    # br.find_element_by_name('historico').send_keys('historico1')
    # br.find_element_by_name('submit').click()
    # setor = Setor.objects.filter(nome = 'setorTeste', sigla = 'ST').exists()
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # assert setor == True
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    # assert br.current_url.endswith('/setor/')

@when('Submeto o cadastro de uma novo setor')
def step_impl(context):
    pass

@then('Recebo uma mensagem de erro informando que o nome do setor ja existe.')
def step_impl(context):
    pass

@then('Nao conseguirei cadastrar o setor ate que eu preencha o campo com diferente.')
def step_impl(context):
    pass





