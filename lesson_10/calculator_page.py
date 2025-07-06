import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """  Конструктор класса CalculatorPage.

        :param driver: WebDriver —  экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 50)

    @allure.step("Открытие страницы логина")
    def open(self):
        """Открывает страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java" +
                        "/slow-calculator.html")

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку на калькуляторе.

        :param seconds: int — задержка в секундах.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажатие кнопки: {value}")
    def press_button(self, value: str) -> None:
        """
        Нажимает кнопку с заданным значением.
        :param value: str — текст кнопки (например, '7', '+', '=')
        """
        button = self.driver.find_element(By.XPATH,
                                          f"//span[text()='{value}']")
        button.click()

    @allure.step("Ожидание появления результата: {expected_result}")
    def get_result(self, expected_result: int) -> bool:
        """
        Ожидает появления заданного результата на экране калькулятора.

        :param expected_result: int — ожидаемое значение.
        :return: bool — True, если результат совпал.
        """
        return self.waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), str(expected_result)
            )
        )
