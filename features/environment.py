from selenium import webdriver
from splinter import Browser
from faker import Faker
import string
import secrets

fake = Faker()

email = fake.email()
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for _ in range(12))


def before_all(context):
    context.web = webdriver.Chrome()
    context.web.maximize_window()
    #context.web = webdriver.Firefox()

def after_step(context, url):
    print()

def after_all(context):
    context.web.quit()

def before_feature(context, feature):
    context.random_email = email
    context.random_password = password
    
