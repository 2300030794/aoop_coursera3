from behave import then
from selenium import webdriver

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source, f'Message "{message}" not found on the page'
