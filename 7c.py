from behave import then
from selenium import webdriver

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    assert text not in context.driver.page_source, f'"{text}" was found on the page but should not be'
