import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(webdriver.FirefoxOptions())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total_price(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    cart.click_checkout()

    checkout.fill_information("Татьяна", "Меркулова", "603000")
    total_text = checkout.get_total()

    assert total_text == "Total: $58.29", \
        f"Ожидаемая сумма: $58.29, но получено: {total_text}"
