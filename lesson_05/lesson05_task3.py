from time import sleep  # импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://the-internet.herokuapp.com/inputs")
tag_name_inp = driver.find_element(By.CSS_SELECTOR, 'input')
tag_name_inp.send_keys("Sky")
sleep(1)
tag_name_inp.clear()
sleep(1)
tag_name_inp.send_keys("Pro")


driver.quit()
