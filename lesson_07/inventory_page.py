from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        item_ids = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie"
        }
        self.driver.find_element(By.CSS_SELECTOR, item_ids[item_name]).click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.shopping_cart_link').click()
