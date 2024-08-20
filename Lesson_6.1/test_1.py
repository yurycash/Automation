from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from time import sleep


def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    
    chrome_browser.find_element(By.CSS_SELECTOR, "input[name=\"first-name\"]").send_keys(first_name)
    chrome_browser.find_element(By.NAME, "last-name").send_keys(last_name)
    chrome_browser.find_element(By.NAME, "address").send_keys(address)
    chrome_browser.find_element(By.NAME, "e-mail").send_keys(email)
    chrome_browser.find_element(By.NAME, "phone").send_keys(phone)
    chrome_browser.find_element(By.NAME, "zip-code").send_keys(zip_code)
    chrome_browser.find_element(By.NAME, "city").send_keys(city)
    chrome_browser.find_element(By.NAME, "country").send_keys(country)
    chrome_browser.find_element(By.NAME, "job-position").send_keys(job_posititon)
    chrome_browser.find_element(By.NAME, "company").send_keys(company)
    
    WebDriverWait(chrome_browser, 40, 0.1).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(20)

    field_classes = {
            "zip-code": "danger",  # Красный
            "first-name": "success",
            "last-name": "success",
            "address": "success",
            "e-mail": "success",
            "phone": "success",
            "city": "success",
            "country": "success",
            "job-position": "success",
            "company": "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in chrome_browser.find_element(
            By.ID, field_id).get_attribute("class")
