import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get('https://rp-cart.x-coding.pl/pl/user')
    browser.delete_cookie('uc_rodo_id')
    cookie = {'name': 'uc_rodo_id',
              'value': 'ex_kc2bm8fo_ffg7b6sa',
              'domain': '.rp-cart.x-coding.pl'}
    browser.add_cookie(cookie)
    browser.refresh()

    wait = WebDriverWait(browser, 10)
    login_button = (By.CLASS_NAME, 'rw-form__button')
    wait.until(expected_conditions.element_to_be_clickable(login_button))

    yield browser
    browser.quit()

def test_should_open_registration(browser):
    registration_tab = browser.find_element_by_css_selector('a:not(.v-tabs__item--active).v-tabs__item')
    registration_tab.click()

    wait = WebDriverWait(browser, 5)
    register_button = (By.CLASS_NAME, 'v-btn__content')
    wait.until(expected_conditions.element_to_be_clickable(register_button))

    register_button = browser.find_element_by_class_name('v-btn__content')
    register_button.click()

    wait = WebDriverWait(browser, 30)
    registration_modal = (By.ID, 'registration-modal')
    wait.until(expected_conditions.element_to_be_clickable(registration_modal))

    id_input = browser.find_element_by_css_selector("[aria-label='NIP** / ID Number *']")
    id_input.send_keys('8822115443')

    login_input = browser.find_element_by_css_selector(("[aria-label='Login *']"))
    login_input.send_keys('tester72')

    password_input = browser.find_element_by_css_selector("[aria-label='Hasło *']")
    password_input.send_keys('testowanie')

    repeat_password_input = browser.find_element_by_css_selector("[aria-label='Powtórz hasło *']")
    repeat_password_input.send_keys('testowanie')

    name_input = browser.find_element_by_css_selector("[aria-label='Imię *']")
    name_input.send_keys('Ada')

    last_name_input = browser.find_element_by_css_selector("[aria-label='Nazwisko *']")
    last_name_input.send_keys('Czekalska')

    email_input = browser.find_element_by_css_selector("[aria-label='E-mail *']")
    email_input.send_keys('a.czekalska@xcitstudio.com')

    telephone_input = browser.find_element_by_css_selector("[aria-label='Telefon kontaktowy *']")
    telephone_input.send_keys('535558353')

    next_button = browser.find_element_by_class_name('v-btn__content')
    next_button.click()

