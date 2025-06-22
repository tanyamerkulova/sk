from time import sleep  # импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("http://uitestingplayground.com/classattr")
tag_name_inp = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
sleep(3)
