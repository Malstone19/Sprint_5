from locators import TestLocators


def test_buns_tab_in_builder_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*TestLocators.SAUCES_TAB).click()
    assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.BUNS_TAB).get_attribute('class')

    driver.find_element(*TestLocators.BUNS_TAB).click()
    assert 'tab_tab_type_current' in driver.find_element(*TestLocators.BUNS_TAB).get_attribute('class')


def test_sauces_tab_in_builder_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.SAUCES_TAB).get_attribute('class')

    driver.find_element(*TestLocators.SAUCES_TAB).click()
    assert 'tab_tab_type_current' in driver.find_element(*TestLocators.SAUCES_TAB).get_attribute('class')


def test_toppings_tab_in_builder_success(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    assert 'tab_tab_type_current' not in driver.find_element(*TestLocators.TOPPINGS_TAB).get_attribute('class')

    driver.find_element(*TestLocators.TOPPINGS_TAB).click()
    assert 'tab_tab_type_current' in driver.find_element(*TestLocators.TOPPINGS_TAB).get_attribute('class')
