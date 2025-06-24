import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox(webdriver.FirefoxOptions())
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    waiter = WebDriverWait(driver, 20)
    # Авторизуйтесь как пользователь
    driver.find_element(By.CSS_SELECTOR,
                        '#user-name').send_keys("standard_user")
    password = 'secret_sauce'
    driver.find_element(By.CSS_SELECTOR,
                        '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,
                        '#login-button').click()
    # Добавьте в корзину товары
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR,
                        '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR,
                        '.shopping_cart_link').click()

    driver.find_element(By.CSS_SELECTOR,
                        '#checkout').click()
    # Заполните форму своими данными
    driver.find_element(By.CSS_SELECTOR,
                        '#first-name').send_keys("Татьяна")
    driver.find_element(By.CSS_SELECTOR,
                        '#last-name').send_keys("Меркулова")
    driver.find_element(By.CSS_SELECTOR,
                        '#postal-code').send_keys("603000")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
    driver.find_element(By.CSS_SELECTOR, '.summary_total_label')
    # Проверьте, что итоговая сумма равна $58.29
    result = waiter.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.summary_total_label'), "Total: $58.29"))
    assert result
