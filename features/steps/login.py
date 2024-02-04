import time

from behave import given, when, then

tempo: int = 1


@given('que abro a url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('preencho o campo email "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='email']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('preencho o campo senha "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='password']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('pressiono o botão Entrar')
def click_button(context):
    button = context.web.find_element("xpath", "//button[@type='submit']")
    time.sleep(tempo)
    button.click()
    button.click()


@then('o sistema apresenta a pagina inicial')
def should_have_title(context):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    assert context.web.find_element("xpath", "//*[@id='root']/div/div/h1").text


@then('aciono o botao listar')
def click_button(context):
    button = context.web.find_element("xpath", "//*[@id='root']/div/div/p[2]/div[3]/div/div/a")
    time.sleep(tempo)
    button.click()
    button.click()


@then('a lista e apresentada')
def should_have_title(context):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    assert context.web.find_element("xpath", "//*[@id='root']/div/div/h1").text
