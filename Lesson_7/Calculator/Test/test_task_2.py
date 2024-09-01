from selenium import webdriver
from Lesson_7.Calculator.Page.MainPageTask_2 import MainPageTask2


def test_calculator():
    browser = webdriver.Chrome()
    main_page = MainPageTask2(browser)
    main_page.clear()
    main_page.data()
    result = main_page.txt()

    assert "15" in result

    browser.quit()
