from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner


# NOTE
# setUp runs before every test method
# tearDown runs after every test method

class AmazonShopping(unittest.TestCase):
    base_url = 'https://www.amazon.com/'
    search_term = 'Logitech Mechanical Keyboard'

    def setUp(self):
        s = Service('/Users/joseservin/PythonProjects/SeleniumBot/drivers/chromedriver')
        options = webdriver.ChromeOptions()
        # DETACH OPTION ALLOWS CHROMEDRIVER TO STAYS OPEN
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_01_load_home_page(self):
        """Webdriver loads Amazon.com """
        # CREATING LOCAL REFERENCE OF DRIVER THAT WAS SET UP
        driver = self.driver
        driver.get(AmazonShopping.base_url)
        self.assertIn('Amazon', driver.title)

    def test_02_item_searching(self):
        """Searching for item defined in search_term variable"""
        driver = self.driver
        driver.get(AmazonShopping.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonShopping.search_term)
        search_box.send_keys(Keys.ENTER)

        self.assertIn(f"Amazon.com : {AmazonShopping.search_term}", driver.title)
        self.assertNotIn('No results found', driver.page_source)

    def test_03_add_to_cart(self):
        """Adding item to cart and handling protection plan"""
        # FOR EVERY TEST WE NEED TO NAVIGATE TO THE WEBPAGE
        driver = self.driver
        driver.get(AmazonShopping.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonShopping.search_term)
        search_box.send_keys(Keys.ENTER)

        # FIND FIRST ITEM
        # time.sleep(2) NOT NEEDED
        my_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logitech K845 Mechanical')))
        my_item.click()

        # ADD ELEMENT TO CART
        cart_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
        cart_button.click()

        # SELECT NO PROTECTION PLAN
        # time.sleep(1) NOT NEEDED IF WE INCREASE WEBDRIVERWAIT TIME
        time.sleep(1)
        no_coverage_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')))
        no_coverage_button.click()

        # ASSERT ACTIONS WERE PERFORMED
        time.sleep(1)
        cart_count_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'nav-cart-count')))
        cart_count = '1'
        message = f"The cart element shows {cart_count_element} but the cart count should be {cart_count}. "
        self.assertEqual(cart_count_element.text, cart_count, message)

    def test_04_delete_item(self):
        """Add item to cart and then delete from cart """
        driver = self.driver
        driver.get(AmazonShopping.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonShopping.search_term)
        search_box.send_keys(Keys.ENTER)

        # FIND FIRST ITEM
        # time.sleep(2) NOT NEEDED
        my_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logitech K845 Mechanical')))
        my_item.click()

        # ADD ELEMENT TO CART
        cart_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
        cart_button.click()

        # SELECT NO PROTECTION PLAN
        # time.sleep(1) NOT NEEDED IF WE INCREASE WEBDRIVERWAIT TIME
        time.sleep(1)
        no_coverage_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')))
        no_coverage_button.click()

        # NAVIGATE TO CART AFTER SELECTING ITEM
        go_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Go to Cart')))
        go_to_cart_button.click()

        time.sleep(2)  # added a longer wait time so the element can be found
        delete_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input')))
        delete_button.click()

        # ALLOW TIME FOR EMPTY CART MESSAGE TO SHOW UP
        time.sleep(2)

        # ASSERT STATEMENTS
        empty_cart_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sc-active-cart"]/div/div/div/h1')))
        empty_cart_message = empty_cart_message.text
        expected_text = 'Your Amazon Cart is empty.'
        error_message = f"Empty cart message shows {empty_cart_message} instead of {expected_text}"
        self.assertEqual(empty_cart_message, expected_text, error_message)

    def test_05_checkout(self):
        """Find and add product to cart as well as proceed to checkout. """
        driver = self.driver
        driver.get(AmazonShopping.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonShopping.search_term)
        search_box.send_keys(Keys.ENTER)

        # FIND FIRST ITEM
        # time.sleep(2) NOT NEEDED
        my_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logitech K845 Mechanical')))
        my_item.click()

        # ADD ELEMENT TO CART
        cart_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
        cart_button.click()

        # SELECT NO PROTECTION PLAN
        # time.sleep(1) NOT NEEDED IF WE INCREASE WEBDRIVERWAIT TIME
        time.sleep(1)
        no_coverage_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')))
        no_coverage_button.click()

        # CHECKOUT
        time.sleep(1)
        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')))
        checkout_button.click()

        # ASSERT WE ARE IN THE LOG-IN PAGE
        self.assertIn('Amazon Sign-In', driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/joseservin/PythonProjects/SeleniumBot/reports'))
