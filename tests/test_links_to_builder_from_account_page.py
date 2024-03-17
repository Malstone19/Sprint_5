from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def test_builder_link_account_page_successful_transition(driver, account_page):
    driver.find_element(*TestLocators.BUILDER_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_logo_link_account_page_successful_transition(driver, account_page):
    driver.find_element(*TestLocators.LOGO_LINK).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_ON_MAIN_PAGE))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
