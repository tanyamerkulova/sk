import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Конструктор страницы корзины.

        :param driver: WebDriver — экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки 'Checkout'")
    def click_checkout(self) -> None:
        """
        Переход к оформлению заказа.
        """
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
