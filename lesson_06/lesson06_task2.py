from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Подавить лишние логи
options = Options()
options.add_argument("--log-level=3")

browser = webdriver.Chrome(service=ChromeService
                           (ChromeDriverManager().install()), options=options)

browser.get("http://uitestingplayground.com/textinput")

# Найти элемент
element = browser.find_element(By.CSS_SELECTOR, '.form-control')
# Очистить элемент
element.clear()
# Отправить данные
element.send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, '.btn').click()

print(browser.find_element(By.CSS_SELECTOR, '.btn').text)

browser.quit()
