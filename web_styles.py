from behave import when
from selenium import webdriver

@when('I press the {button_name} button')
def step_impl(context, button_name):
    button = context.driver.find_element("xpath", f"//button[text()='{button_name}']")
    button.click()
