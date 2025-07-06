import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор страницы логина.

        :param driver: WebDriver — экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Открытие страницы логина")
    def open(self):
        """ Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация с логином: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: str — имя пользователя.
        :param password: str — пароль пользователя.
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#login-button').click()
