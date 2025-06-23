from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# Подавить лишние логи
options = Options()
options.add_argument("--log-level=3")

browser = webdriver.Chrome(service=ChromeService
                           (ChromeDriverManager().install()), options=options)

browser.get("http://uitestingplayground.com/ajax")

waiter = WebDriverWait(browser, 40)

browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".bg-success"),
                                     "Data loaded with AJAX get request."))
print(browser.find_element(By.CSS_SELECTOR, '.bg-success ').text)

browser.quit()
