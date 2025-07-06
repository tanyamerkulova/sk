import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы WebDriver.
    """
    driver = webdriver.Firefox(webdriver.FirefoxOptions())
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы на странице оформления заказа")
@allure.description("Добавляем товары, " +
                    "проходим авторизацию, оформляем заказ, проверяем сумму.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.BLOCKER)
def test_total_price(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Авторизация в системе"):
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("ДДобавление товаров в корзину"):
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")

    with allure.step("Переход в корзину"):
        inventory.go_to_cart()

    with allure.step("Нажатие 'Checkout'"):
        cart.click_checkout()

    with allure.step("Заполнение данные покупателя"):
        checkout.fill_information("Татьяна", "Меркулова", "603000")

    with allure.step("Получение и проверка итоговой суммы"):
        total_text = checkout.get_total()
    assert total_text == "Total: $58.29", (
        f"Ожидаемая сумма: $58.29, но получено: {total_text}"
    )
