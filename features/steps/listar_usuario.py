import time

from behave import given, when, then

tempo: int = 1


@given('que visito a url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('insiro o email "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='email']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('insiro a senha "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='password']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('clico no botão Entrar')
def click_button(context):
    button = context.web.find_element("xpath", "//button[@type='submit']")
    time.sleep(tempo)
    button.click()
    button.click()


@when('aciono o botao listar')
def click_button(context):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    #button = context.web.find_element("xpath", "//a[@data-testid='listarUsuarios']")
    button = context.web.find_element("xpath", "//a[@data-testid='listarUsuarios']")
    time.sleep(tempo)
    button.click()


@then('o usuario "{value}" e apresentado na lista')
def should_have_title(context, value):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    assert context.web.find_element("xpath", "//*[text()='" + value + "']")
