from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.XPATH, "(//a[contains(@href, '/basket/')])[1]")

class BasketPageLocators():
    CART_WITH_PRODUCTS = (By.CSS_SELECTOR, "form#basket_formset")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CART= (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    MESSAGE_CART_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".product-card.alert-success")