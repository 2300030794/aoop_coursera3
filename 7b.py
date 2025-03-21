from behave import then
from selenium import webdriver

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.driver.page_source, f'"{text}" not found on the page'
