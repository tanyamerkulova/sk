from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, value):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self, expected_result):
        return self.waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), str(expected_result)
            )
        )
