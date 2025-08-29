from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def should_be_massage_about_adding_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name in message_name, \
            f"Product name in message is wrong: expected {product_name}, got {message_name}"

    def should_be_correct_products_price_in_cart(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_TOTAL).text
        assert product_price == cart_total, \
            f"Basket total is wrong: expected {product_price}, got {cart_total}"

    def should_not_have_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should NOT be"

    def success_message_should_disappear(self, timeout=4):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout=timeout), \
            "Success message did not disappear"
