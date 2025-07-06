import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор страницы оформления заказа.

        :param driver: WebDriver — экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы оформления: " +
                 "{first_name} {last_name}, {postal_code}")
    def fill_information(self, first_name: str, last_name: str,
                         postal_code: str) -> None:
        """
        Заполняет форму данных пользователя и нажимает Continue.
        :param first_name: str — имя
        :param last_name: str — фамилия
        :param postal_code: str — почтовый индекс
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#continue').click()

    @allure.step("Получение итоговой суммы")
    def get_total(self) -> str:
        """
        Получает итоговую сумму на странице.

        :return: str — текст с итоговой суммой.
        """
        total = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            '.summary_total_label')))
        return total.text
