from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

fake = Faker()

@given('que acesso a url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('aciono o link de cadastro')
def click_button(context):
    wait = WebDriverWait(context.web, 10)
    register_link = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='root']/div/div/form/small/a")))
    register_link.click()


@when('informo o campo nome')
def fill_field(context):
    context.random_name = fake.name()
    wait = WebDriverWait(context.web, 10)
    name_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='nome']")))
    name_field.click()
    name_field.clear()
    name_field.send_keys(context.random_name)


@when('informo o campo email')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    email_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='email']")))
    email_field.click()
    email_field.clear()
    email_field.send_keys(context.random_email)


@when('informo o campo senha')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    password_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='password']")))
    password_field.click()
    password_field.clear()
    password_field.send_keys(context.random_password)


@when('seleciono o check Cadastrar como administrador')
def click_checkbox(context):
    wait = WebDriverWait(context.web, 10) 
    checkbox = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='administrador']"))) 
    checkbox.click()


@when('aciono o botao Cadastrar')
def click_button(context):
    wait = WebDriverWait(context.web, 10)
    button = context.web.find_element("xpath", "//*[@id='root']/div/div/form/div[5]/button")
    button.click()


@then('o sistema apresenta as boas vindas para o usuario')
def should_have_title(context):
    wait = WebDriverWait(context.web, 10) 
    welcome_text = wait.until(EC.visibility_of_element_located(("xpath", "//*[text()='" + context.random_name + "']"))) 
    assert welcome_text
