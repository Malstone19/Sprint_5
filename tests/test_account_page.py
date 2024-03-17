from locators import TestLocators


def test_enter_account_page_link_account_success(driver, account_page):
    name = driver.find_element(*TestLocators.NAME_INPUT).get_attribute('value')
    assert name == 'Aleksey'
