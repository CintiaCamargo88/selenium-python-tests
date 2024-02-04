import time

from behave import given, when, then

tempo: int = 1


@given('que acesso a url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('aciono o link de cadastro')
def click_button(context):
    button = context.web.find_element("xpath", "//*[@id='root']/div/div/form/small/a")
    time.sleep(tempo)
    button.click()
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)


@when('informo o campo nome "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='nome']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('informo o campo email "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='email']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('informo o campo senha "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='password']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('seleciono o check Cadastrar como administrador')
def click_checkbox(context):
    checkbox = context.web.find_element("xpath", "//*[@id='administrador']")
    time.sleep(tempo)
    checkbox.click()
    time.sleep(tempo)


@when('aciono o botão Cadastrar')
def click_button(context):
    button = context.web.find_element("xpath", "//*[@id='root']/div/div/form/div[5]/button")
    time.sleep(tempo)
    button.click()


@then('o sistema apresenta as boas vindas para "{value}"')
def should_have_title(context, value):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    assert context.web.find_element("xpath", "//*[text()='" + value + "']")
