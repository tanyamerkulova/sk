import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()))
    # передаем driver для использования в тесте
    # А всё, что после yield, выполнится после теста
    yield driver
    driver.quit()


@pytest.fixture
def form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR,
                        '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR,
                        '[name="company"]').send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()


@pytest.mark.usefixtures("form")
def test_zip_code_invalid_red(driver):
    zip_color = driver.find_element(
        By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    assert zip_color == 'rgba(248, 215, 218, 1)', "Zip не подсвечено красным"


@pytest.mark.usefixtures("form")
def test_all_other_fields_valid_green(driver):
    expected_green = 'rgba(209, 231, 221, 1)'
    valid_fields = [
        "#first-name", "#last-name", "#address", "#e-mail", "#phone",
        "#city", "#country", "#job-position", "#company"
        ]

    for id in valid_fields:
        field = driver.find_element(By.CSS_SELECTOR, id)
        color = field.value_of_css_property('background-color')
        assert color == expected_green, f"Поле '{id}' не зеленое"
