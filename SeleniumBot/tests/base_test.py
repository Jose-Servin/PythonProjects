from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner
from SeleniumBot.resources.pages import BasePage, HomePage, SearchResultsPage, ProductDetail, SubCartPage, MainCartPage, SignInPage
from SeleniumBot.resources.locators import Locators
from SeleniumBot.resources.test_data import TestData


# --- BASE-TEST CLASS CONTAINS SETUP AND TEARDOWN METHODS ---


class TestAmazonSearchBase(unittest.TestCase):
    def setUp(self):
        s = Service(TestData.SERVICE_PATH)
        options = webdriver.ChromeOptions()
        # DETACH OPTION ALLOWS CHROMEDRIVER TO STAYS OPEN
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class TestAmazonSearch(TestAmazonSearchBase):
    """Main test class containing corresponding test cases for POM structure. """

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_home_page_loaded(self):
        """ instantiate an object of HomePage class. Remember when the constructor of HomePage class is called.
        it opens up the browser and navigates to Home Page of the site under test."""

        self.home_page = HomePage(self.driver)
        self.assertIn(TestData.HOME_PAGE_TITLE, self.home_page.driver.title)