from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import TEST_ACCOUNT_PASS


def test_registration_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_PAGE_BUTTON))

    name = f'aleksey_maltsev{randint(100, 999)}'
    email = f'aleksey_maltsev_6_{randint(100, 999)}@gmail.com'

    driver.find_element(*TestLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.PASS_INPUT).send_keys(TEST_ACCOUNT_PASS)

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

    button_text = driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).text
    assert 'https://stellarburgers.nomoreparties.site/login' == driver.current_url and button_text == 'Войти'


def test_registration_incorrect_pass_error_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*TestLocators.NAME_INPUT).send_keys('aleksey_maltsev21421')
    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('aleksey_maltsev@yandex.ru')
    driver.find_element(*TestLocators.PASS_INPUT).send_keys('1')

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()

    assert driver.find_element(*TestLocators.INCORRECT_PASS_ERROR_TEXT).text == 'Некорректный пароль'
