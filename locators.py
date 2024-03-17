from selenium.webdriver.common.by import By


class TestLocators:
    # Поля ввода данных пользователя
    NAME_INPUT = By.XPATH, './/label[text()="Имя"]/parent::div/input'
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/parent::div/input'
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/parent::div/input'

    # Кнопка Войти/Зарегистрироваться
    LOGIN_PAGE_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'

    LINK_TO_LOGIN_PAGE = By.LINK_TEXT, 'Войти'  # Ссылка на страницу авторизации
    TITLE_LOGIN_PAGE = By.XPATH, './/h2[text()="Вход"]'  # Заголовок страницы входа
    ACCOUNT_PAGE_LINK = By.LINK_TEXT, 'Личный Кабинет'  # Ссылка в личный кабинет

    # Сообщение о вводе не корректного пароля, на странице авторизации
    INCORRECT_PASS_ERROR_TEXT = By.XPATH, './/p[contains(@class, "input__error")]'

    # Кнопка войти/оформить заказ на главной
    LOGIN_BUTTON_ON_MAIN_PAGE = By.XPATH, './/button[contains(@class, "button_button_size_large")]'

    BUILDER_LINK = By.LINK_TEXT, 'Конструктор'  # Ссылка на страницу конструктора
    LOGO_LINK = By.XPATH, './/div[contains(@class, "AppHeader_header")]/a'  # Ссылка логотипа
    LOGOUT_BUTTON = By.XPATH, './/button[contains(@class, "Account_button")]'  # Кнопка выхода из аккаунта

    # Вкладки конструктора
    BUNS_TAB = By.XPATH, './/span[text()="Булки"]/parent::div'
    SAUCES_TAB = By.XPATH, './/span[text()="Соусы"]/parent::div'
    TOPPINGS_TAB = By.XPATH, './/span[text()="Начинки"]/parent::div'
