from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# THE KEYS CLASS PROVIDES KEYBOARD KEY VALUES
from selenium.webdriver.common.keys import Keys
import unittest
import time


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

    def test_add_to_cart(self):
        # FOR EVERY TEST WE NEED TO NAVIGATE TO THE WEBPAGE
        driver = self.driver
        driver.get(AmazonItemSearch.base_url)
        self.assertIn('Amazon', driver.title)

        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys(AmazonItemSearch.search_term)
        search_box.send_keys(Keys.ENTER)

        # FIND FIRST ITEM
        # time.sleep(2) NOT NEEDED
        first_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logitech K845 Mechanical')))
        first_item.click()

        # ADD ELEMENT TO CART
        cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
        cart_button.click()

        # SELECT NO PROTECTION PLAN
        # time.sleep(1) NOT NEEDED IF WE INCREASE WEBDRIVERWAIT TIME
        no_coverage_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")))
        no_coverage_button.click()

        # ASSERT ACTIONS WERE PERFORMED

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
