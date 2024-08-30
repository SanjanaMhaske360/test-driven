# features/steps/web_steps.py

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I am on the home page')
def step_given_i_am_on_home_page(context):
    context.browser.get(context.base_url)

@when('I click the "{button_text}" button')
def step_when_i_click_button(context, button_text):
    button = context.browser.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

@then('I should see "{text}" on the page')
def step_then_i_should_see_text(context, text):
    body = context.browser.find_element(By.TAG_NAME, 'body')
    assert text in body.text
