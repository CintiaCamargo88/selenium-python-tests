from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('que visito a url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('insiro o email')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    email_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='email']")))
    email_field.click()
    email_field.clear()
    email_field.send_keys(context.random_email)


@when('insiro a senha')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    password_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='password']")))
    password_field.click()
    password_field.clear()
    password_field.send_keys(context.random_password)


@when('clico no botão Entrar')
def click_button(context):
    wait = WebDriverWait(context.web, 10)
    button = wait.until(EC.visibility_of_element_located(("xpath", "//button[@type='submit']")))
    button.click()


@when('aciono o botao listar')
def click_button(context):
    wait = WebDriverWait(context.web, 10)
    button = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='root']/div/div/p[2]/div[3]/div/div/a")))
    button.click()


@then('o usuario e apresentado na lista')
def should_have_title(context):
    wait = WebDriverWait(context.web, 10) 
    list_email = wait.until(EC.visibility_of_element_located(("xpath", "//*[text()='" + context.random_email + "']")))
    assert list_email
