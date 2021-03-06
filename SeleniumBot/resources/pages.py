from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner
from test_data import TestData
from locators import Locators


class BasePage:
    """
    This class is the parent class for all the pages in our application.
    It contains methods for the most common actions that are expected to be performed on any page in the application.
    """

    def __init__(self, driver):
        """This function is called every time a base class object is created. """
        self.driver = driver

    def click(self, by_locator):
        """This function clicks on elements whose locator is passed as an argument. """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, expected_text):
        """This function asserts comparison between web element text and expected text. """
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == expected_text

    def enter_text(self, by_locator, text):
        """Performs text entry to element specified by locator. """
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return text_box.send_keys(text)

    def is_enabled(self, by_locator):
        """Checks if web element is enabled and returns element """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def is_visible(self, by_locator):
        """Checks if web element passed is visible and return boolean value. """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


class HomePage(BasePage):
    """Home page of Amazon """

    def __init__(self, driver):
        super().__init__(driver)  # THE __init__ arguments of our Parent Class
        self.driver.get(TestData.BASE_URL)  # ARRIVING TO HOME PAGE

    def search(self):
        """Finding the search box element and using it. """
        self.driver.find_element(Locators.SEARCH_BOX).clear()
        self.enter_text(Locators.SEARCH_BOX, TestData.SEARCH_TERM)
        self.driver.find_element(Locators.SEARCH_BOX).send_keys(Keys.ENTER)


class SearchResultsPage(BasePage):
    """Clicking on the item we want after arriving to Search Result page """

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_item(self):
        self.click(Locators.SEARCH_RESULT)  # This 'click' method comes from the parent class.


class ProductDetail(BasePage):
    """Specific Logitech Page for item selected """

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.click(Locators.ADD_TO_CART_BUTTON)

    def click_no_protection_plan(self):
        self.click(Locators.NO_COVERAGE_BUTTON)


class SubCartPage(BasePage):
    """Sub-cart page navigation. """

    def __init__(self, driver):
        super().__init__(driver)

    def click_go_to_cart(self):
        self.click(Locators.GO_TO_CART_BUTTON)

    def click_proceed_to_checkout(self):
        self.click(Locators.CHECKOUT_BUTTON)


class MainCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def delete_item_from_cart(self):
        self.click(Locators.DELETE_ITEM_BUTTON)

    def check_deleted_item(self):
        self.assert_element_text(Locators.EMPTY_CART_MESSAGE, TestData.EXPECTED_EMPTY_CART_MESSAGE)


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
