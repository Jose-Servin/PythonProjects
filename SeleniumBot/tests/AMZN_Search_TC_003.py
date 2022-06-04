from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# THE KEYS CLASS PROVIDES KEYBOARD KEY VALUES
from selenium.webdriver.common.keys import Keys
import unittest


class AmazonItemSearch(unittest.TestCase):
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

    def test_item_searching(self):
        driver = self.driver
        driver.get(AmazonItemSearch.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonItemSearch.search_term)
        search_box.send_keys(Keys.ENTER)

        self.assertIn(f"Amazon.com : {AmazonItemSearch.search_term}", driver.title)
        self.assertNotIn('No results found', driver.page_source)

    def test_add_to_cart(self):
        driver = self.driver
        # FIND FIRST ITEM
        first_item = driver.find_element(By.CLASS_NAME, 'a-section aok-relative s-image-fixed-height')
        first_item.click()

        cart_button = driver.find_element(By.ID, 'add-to-cart-button')
        cart_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
