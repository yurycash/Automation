import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    # firefox.get("http://the-internet.herokuapp.com/entry_ad")
    waitChrome = WebDriverWait(chrome, 10)
    # waitFirefox = WebDriverWait(firefox, 10)
    modal_window = waitChrome.until(
        EC.visiblity_of_elements_located((By.CSS_SELECTOR, ".modal")))
    close_button = waitChrome.until(EC.element_to_by_clicable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_button.click()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
