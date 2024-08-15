from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

firefox.get("https://the-internet.herokuapp.com/login")
firefox.find_element(By.ID, "username").send_keys("tomsmith")
firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(3)
firefox.find_element(By.TAG_NAME, "button").click()

firefox.quit()
