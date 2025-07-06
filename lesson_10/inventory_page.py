import allure
from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        """
        Конструктор страницы списка товаров.

        :param driver: WebDriver — экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину: {item_name}")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param item_name: str — название товара.
        """
        item_ids = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie"
        }
        self.driver.find_element(By.CSS_SELECTOR, item_ids[item_name]).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """Переходит в корзину"""
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.shopping_cart_link').click()
