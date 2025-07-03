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
waiter = WebDriverWait(browser, 40, 0.5)

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!"))

images = browser.find_elements(By.CSS_SELECTOR, "img")[3].get_attribute("src")

print(images)

browser.quit()
