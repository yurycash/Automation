from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

chrome.get("https://the-internet.herokuapp.com/login")
chrome.find_element(By.ID, "username").send_keys("tomsmith")
chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(3)
chrome.find_element(By.TAG_NAME, "button").click()
sleep(2)
