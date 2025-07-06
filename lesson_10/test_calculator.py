import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--log-level=3")  # подавляем лишние логи
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@allure.title("Проверка сложения в калькуляторе")
@allure.description("Тест проверяет правильность работы " +
                    "сложения с задержкой на веб-калькуляторе.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    calculator = CalculatorPage(driver)
    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Ввести выражение 7 + 8 ="):
        calculator.press_button("7")
        calculator.press_button("+")
        calculator.press_button("8")
        calculator.press_button("=")

    with allure.step("Проверить, что результат равен 15"):
        assert calculator.get_result(15), "Результат должен быть равен 15"
