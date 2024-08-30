# features/steps/web_steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on the "{page_name}" page')
def step_given_i_am_on_page(context, page_name):
    context.browser.get(context.base_url + '/' + page_name)

@then('I should see "{text}" on the page')
def step_then_i_should_see_text(context, text):
    body = context.browser.find_element(By.TAG_NAME, 'body')
    assert text in body.text, f'Expected text "{text}" not found on the page'
