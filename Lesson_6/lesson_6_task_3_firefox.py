from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 20, 0.1)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done'))
print(driver.find_element(By.ID, "award").get_attribute("src"))

driver.quit()
