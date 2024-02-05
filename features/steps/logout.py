import time

from behave import given, when, then

tempo: int = 1


@given('que entro na url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('preencho o email "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='email']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('preencho a senha "{value}"')
def fill_field(context, value):
    input_field = context.web.find_element("xpath", "//*[@id='password']")
    time.sleep(tempo)
    input_field.click()
    input_field.clear()
    time.sleep(tempo)
    input_field.send_keys(value)


@when('pressiono Entrar')
def click_button(context):
    button = context.web.find_element("xpath", "//button[@type='submit']")
    time.sleep(tempo)
    button.click()
    button.click()


@when('apresenta a pagina inicial')
def should_have_title(context):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    assert context.web.find_element("xpath", "//*[@id='root']/div/div/h1").text


@then('aciono logout')
def click_button(context):
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    time.sleep(tempo)
    button1 = context.web.find_element("xpath", "//*[@id='navbarTogglerDemo01']")
    button1.click()
    time.sleep(tempo)
    time.sleep(tempo)
    button2 = context.web.find_element("xpath", "//form/button[@type='button']")
    time.sleep(tempo)
    button2.click()
