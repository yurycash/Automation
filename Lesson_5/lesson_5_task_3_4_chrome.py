import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(chrome, 10)

    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_button.click()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
