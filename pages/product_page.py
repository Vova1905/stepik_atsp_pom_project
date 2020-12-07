from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        # BasePage.solve_quiz_and_get_code(self)

    def should_be_product_in_basket_and_correct_cost(self):
        assert self.browser.find_element(*ProductPageLocators.BOUGHT_TITLE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text, "Wrong bought title"
        assert self.browser.find_element(*ProductPageLocators.PRICE_TEXT).text in self.browser.find_element(*ProductPageLocators.BASKET_COST).text, "Wrong basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disapperead_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappear"
