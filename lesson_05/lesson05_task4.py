from time import sleep  # импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get(" http://the-internet.herokuapp.com/login")

tag_name_inp = driver.find_element(By.CSS_SELECTOR, '#username')
tag_name_inp.send_keys("tomsmith")
sleep(2)
tag_name_inp = driver.find_element(By.CSS_SELECTOR, '#password')
tag_name_inp.send_keys("SuperSecretPassword!")
sleep(2)
tag_name_inp = driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
sleep(2)

txt = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(txt)
sleep(2)

driver.quit()
