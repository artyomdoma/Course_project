import pytest
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import time



PRODUCT_URL = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_massage_about_adding_to_cart()
    page.should_be_correct_products_price_in_cart()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="Сообщение появляется после добавления в корзину")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_to_cart()
    page.should_not_have_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.should_not_have_success_message()

@pytest.mark.xfail(reason="Сообщение не исчезает автоматически на этой странице.")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.add_to_cart()
    page.success_message_should_disappear(timeout=4)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.open_cart_link()
    basket_page = BasketPage(browser, PRODUCT_URL)
    basket_page.is_not_element_present_in_cart()
    basket_page.empty_basket_message()

