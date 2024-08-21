# from time import sleep
from selenium import webdriver
from Lesson_7.SwagLabs.Page.Main_Page import MainPage
from Lesson_7.SwagLabs.Page.products import Products
from Lesson_7.SwagLabs.Page.Cart import YourCart
from Lesson_7.SwagLabs.Page.DataOrder import Data
from Lesson_7.SwagLabs.Page.Check import Checkout


def test_shopping():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.authorization()

    product = Products(browser)
    product.add_shopping()

    cart = YourCart(browser)
    cart.get()
    cart.checkout()

    data = Data(browser)
    data.data_order()
    data.continue_button()

    check = Checkout(browser)
    total = check.summary_total()
    assert '58.29' in total

    browser.quit()
