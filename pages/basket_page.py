from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_element_present_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_WITH_PRODUCTS), \
            "Products is not present in cart"

    def empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY),\
            "Empty basket message is presented"