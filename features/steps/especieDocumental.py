from behave import given, when, then
from test.factories.user import UserFactory
from test.factories.especieDocumental import EspecieDocumentalFactory
from app.models import EspecieDocumental

#Scenario: Campos Vazios
@given('Eu sou um usuario logado')
def step_impl(context):
    #Cria um usuário de teste
    criarNovoUsuario()

    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('action').click()



def criarNovoUsuario():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    # Don't omit to call save() to insert object in database
    u.save()

def criarEspecieDocumental():
    especie = EspecieDocumental()
    especie.nome= "Teste"
    especie.save()

@given('Estou na pagina de cadastro de uma especie documental')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/especieDocumental/')

@when('Submeto o cadastro de uma nova especie documental deixando o campo em branco')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()

@then('Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/especieDocumental/')
    assert br.find_element_by_id('nome').text == ""

#Scenario: Cadastrar nova EspecieDocumental
@when('Informo um nome ainda nao cadastrado no sistema')
def step_impl(context):
    br = context.browser
    especie = EspecieDocumental.objects.filter(nome='Folha de Ponto').exists()
    assert especie == False

@when('Submeto o cadastro de uma nova especie')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('nome').send_keys('Folha de Ponto')
    br.find_element_by_name('submit').click()
    # br.get_screenshot_as_file('/tmp/screenshot.png')

@then('Sou redirecionado para a pagina principal de especie documental')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('A especie devera estar devidamente cadastrada.')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')
    assert br.find_element_by_id('nomeEspecie').text == "Folha de Ponto"

@when('Informo um nome ja cadastrado no sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')
    especie = EspecieDocumental.objects.filter(nome='Folha de Ponto').exists()
    assert  especie == True

@then('Recebo uma mensagem de erro informando que o nome ja existe.')
def step_impl(context):
    br = context.browser

    message = br.find_element_by_id('mensagem').text
    assert br.current_url.endswith('/especieDocumental/')
    assert message == "A Especie Documental ja existe. Por favor, tente novamente!"


@then('Nao conseguirei cadastrar a especie ate que eu preencha o com um nome diferente.')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/especieDocumental/')

#Scenario: Editar Especie documental
@given('Estou na pagina com a lista de especies documentais')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/especiesDocumentais_list')
    # Checks success status
        assert br.current_url.endswith('/especiesDocumentais_list/')

@given('Possue uma ou mais especies documentais cadastradas')
def step_impl(context):
        criarEspecieDocumental()
        br = context.browser
        especie = EspecieDocumental.objects.filter(nome='Teste').exists()
        assert especie==True


@when('Seleciono o botao editar de uma especie documental')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/especiesDocumentais_list')
        br.find_element_by_name('editar').click()

@when('Sou redirecionado para a pagina com seus dados ja preenchidos')
def step_impl(context):
        br = context.browser
        especie = EspecieDocumental.objects.get(nome='Teste')
        br.get(context.base_url + '/especieDocumental/%d/edit' % especie.id)
        assert br.current_url.endswith('/especieDocumental/%d/edit/' % especie.id)


@when ('Preencho os campos obrigatorios')
def step_impl(context):
        br = context.browser
        assert br.find_element_by_name('nome').text != ""

@when('Clico no botao salvar')
def step_impl(context):
        br = context.browser
        br.find_element_by_id('salvar').click()

#Scenario: Visualizar Especie Documental
@given('Uma nova especie documental foi criada')
def step_impl(context):
    br = context.browser

    criarNovaEspecieDocumental()

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabe()

    br.find_element_by_name('nome').send_keys('Ata')
    br.find_element_by_name('submit').click()


def criarNovaEspecieDocumental():


@when('Escolho visualizar a lista de especies documentais')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/especiesDocumentais_list')
    assert br.current_url.endswith('/especiesDocumentais_list')


@then
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/especiesDocumentais_list')
    assert br.find_element_by_id('nomeEspecie').text == 'Ata'

#Scenario: Excluir Especie documental
@given('que existem especies documentais cadastradas')
def step_impl(context):
        br = context.browser
        especieDocumentalFactory(3)
        br.refresh()
        assert EspecieDocumental.objects.count()==3
        assert EspecieDocumental.objects.filter(nome='especie0').exists()
        assert EspecieDocumental.objects.filter(nome='especie1').exists()
        assert EspecieDocumental.objects.filter(nome='especie2').exists()
        assert br.current_url.endswith('/especiesDocumentais_list/')

def especieDocumentalFactory(quantidade):
    for index in range(quantidade):
        nomeEspecie = 'especie' + str(index)
        especie = EspecieDocumentalFactory(nome=nomeEspecie)
        especie.save()


@when('clico no botao excluir')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('excluir').click()
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('a especie documental deixara de existir.')
def step_impl(context):
        br = context.browser

        br.refresh()
        assert EspecieDocumental.objects.count() == 2

