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


def test_calculator_addition(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay(45)
    calculator.press_button("7")
    calculator.press_button("+")
    calculator.press_button("8")
    calculator.press_button("=")

    assert calculator.get_result(15), "Результат должен быть равен 15"
