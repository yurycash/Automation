from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.get("https://the-internet.herokuapp.com/inputs")
input_field = chrome.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
input_field.clear()
input_field.send_keys("999")
