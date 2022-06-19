from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner


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
