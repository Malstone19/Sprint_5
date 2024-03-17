from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
import data


def test_login_button_on_main_page_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.TEST_ACCOUNT_EMAIL)
    driver.find_element(*TestLocators.PASS_INPUT).send_keys(data.TEST_ACCOUNT_PASS)

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    button_text = driver.find_element(*TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE).text
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and button_text == 'Оформить заказ'


def test_login_in_account_page_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*TestLocators.ACCOUNT_PAGE_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.TEST_ACCOUNT_EMAIL)
    driver.find_element(*TestLocators.PASS_INPUT).send_keys(data.TEST_ACCOUNT_PASS)

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    button_text = driver.find_element(*TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE).text
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and button_text == 'Оформить заказ'


def test_login_in_registration_page_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*TestLocators.LINK_TO_LOGIN_PAGE).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.TEST_ACCOUNT_EMAIL)
    driver.find_element(*TestLocators.PASS_INPUT).send_keys(data.TEST_ACCOUNT_PASS)

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    button_text = driver.find_element(*TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE).text
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and button_text == 'Оформить заказ'


def test_login_forgot_pass_page_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(*TestLocators.LINK_TO_LOGIN_PAGE).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.TITLE_LOGIN_PAGE))

    driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.TEST_ACCOUNT_EMAIL)
    driver.find_element(*TestLocators.PASS_INPUT).send_keys(data.TEST_ACCOUNT_PASS)

    driver.find_element(*TestLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    button_text = driver.find_element(*TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE).text
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and button_text == 'Оформить заказ'
