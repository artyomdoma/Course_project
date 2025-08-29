from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators, MainPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.go_to_login_page()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_url(self):
        current = self.browser.current_url
        assert "login" in current, \
            f"Login page did not contain 'login' in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            f"Login form did not contain 'login' in {self.browser.current_url}"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            f"Register form did not contain 'register' in {self.browser.current_url}"