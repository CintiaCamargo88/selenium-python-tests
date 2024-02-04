from selenium import webdriver
from splinter import Browser


def before_all(context):
    context.web = webdriver.Chrome()
    context.web.maximize_window()
    #context.web = webdriver.Firefox()


def after_step(context, url):
    print()



def after_all(context):
    context.web.quit()
