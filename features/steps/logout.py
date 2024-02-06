from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('que entro na url "{url}"')
def visit_page(context, url):
    context.web.get(url)


@when('preencho o email')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    email_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='email']")))
    email_field.click()
    email_field.clear()
    email_field.send_keys(context.random_email)


@when('preencho a senha')
def fill_field(context):
    wait = WebDriverWait(context.web, 10)
    password_field = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='password']")))
    password_field.click()
    password_field.clear()
    password_field.send_keys(context.random_password)


@when('pressiono Entrar')
def click_button(context):
    wait = WebDriverWait(context.web, 10)
    button = wait.until(EC.visibility_of_element_located(("xpath", "//button[@type='submit']")))
    button.click()


@when('apresenta a pagina inicial')
def should_have_title(context):
    wait = WebDriverWait(context.web, 10) 
    welcome_text = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='root']/div/div/h1")))
    assert welcome_text


@then('aciono logout')
def click_button(context):
    wait = WebDriverWait(context.web, 10) 
    button1 = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='navbarTogglerDemo01']")))
    button1.click()
    wait = WebDriverWait(context.web, 10) 
    button2 = wait.until(EC.visibility_of_element_located(("xpath", "//form/button[@type='button']")))
    button2.click()
