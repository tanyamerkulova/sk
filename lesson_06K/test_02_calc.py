import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#  Подавить лишние логи
options = Options()
options.add_argument("--log-level=3")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()), options=options)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calc(driver):
    waiter = WebDriverWait(driver, 50, 0.5)

    delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.CSS_SELECTOR,
                        'span.btn.btn-outline-primary:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR,
                        'span.operator.btn.btn-outline-success').click()
    driver.find_element(By.CSS_SELECTOR,
                        'span.btn.btn-outline-primary:nth-child(2)').click()
    driver.find_element(By.CSS_SELECTOR,
                        'span.btn.btn-outline-warning').click()

    result = waiter.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'div.screen'), "15"))
    assert result
