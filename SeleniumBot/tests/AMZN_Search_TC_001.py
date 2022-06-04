from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest


# INHERITING TestCase IS HOW UNITTEST KNOWS THIS IS A TEST CASE
class AmazonHomePage(unittest.TestCase):
    base_url = 'https://www.amazon.com/'

    # --- HERE WE CREATE/INITIALIZE THE DRIVER AND SET ANY PROPERTIES
    def setUp(self):
        s = Service('/Users/joseservin/PythonProjects/SeleniumBot/drivers/chromedriver')
        options = webdriver.ChromeOptions()
        # DETACH OPTION ALLOWS CHROMEDRIVER TO STAYS OPEN
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # --- PERFORM AUTOMATION ACTION AND ANY TESTS
    def test_load_home_page(self):
        # CREATING LOCAL REFERENCE OF DRIVER THAT WAS SET UP
        driver = self.driver
        driver.get(AmazonHomePage.base_url)
        self.assertIn('Amazon', driver.title)

    # --- CLOSE THE BROWSER
    def tearDown(self):
        self.driver.close()

    # TERMINAL COMMAND USED TO ALLOW CHROME DRIVER xattr -d com.apple.quarantine <PATH TO DRIVER>
    # driver.close()


if __name__ == "__main__":
    unittest.main()
