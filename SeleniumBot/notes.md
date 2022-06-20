# Selenium POM Framework 

Currently, we have stand-alone test cases which require us to repeat processes already performed in earlier tests. <br>


## Methodology 
1. Examine which pages are being used/visited for each test case. 

For example:
* test_01: home_page, 
* test_02: home_page, item_page
* test_03: home_page, item_page, sub_cart_page, user_login 

Here we can see that `home_page` is being used in all three tests, therefore with our current framework we have lost 
of duplicate code and are very error-prone. 


## POM Structure
```
(Project Name)
|- Drivers
|- Reports
|- Resources
 |- PO (page objects)
|- Tests
```

## POM File Setup 

`testdata.py` <br>

This file holds search terms, strings, numbers, global variables etc. 
```python
class TestData:
    BASE_URL = 'https://www.amazon.com/'
    SEARCH_TERM = 'Logitech Mechanical Keyboard'
    HOME_PAGE_TITLE = 'Amazon'
    NO_RESULTS_FOUND = 'No results found'
    EXPECTED_CART_COUNT = '1'
    EXPECTED_EMPTY_CART_MESSAGE = 'Your Amazon Cart is empty.'
    SIGN_IN_PAGE_TITLE = 'Amazon Sign-In'
    SERVICE_PATH = '/Users/joseservin/PythonProjects/SeleniumBot/drivers/chromedriver'
```

`locators.py` <br>

This file holds all locators for webpage elements. This creates a single point of reference in case we need to 
update elements. Here we follow proper naming convention, using all capital letters. The strategy used to create 
this was examining each test case and identifying the different pages visited. Next, we grab all instances where an 
element is being identified and re-define them in this locators file. 

```python
from selenium.webdriver.common.by import By

class Locators:
    # --- Home Page Locators ---
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')

    # -- ITEM SEARCH PAGE --
    SEARCH_RESULT = (By.PARTIAL_LINK_TEXT, 'Logitech K845 Mechanical')

    # -- PRODUCT DETAIL PAGE --
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    NO_COVERAGE_BUTTON = (By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')
    CART_COUNT = (By.ID, 'nav-cart-count')

    # -- SUB CART PAGE --
    GO_TO_CART_BUTTON = (By.LINK_TEXT, 'Go to Cart')
    DELETE_ITEM_BUTTON = (By.XPATH,
                          '/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input')
    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')

    # -- EMPTY CART PAGE --
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div/h1')
```

`pages.py` <br>

This file will contain all page classes. For simplicity, we are following this best practice, but we can easily 
separate the pages via file creations. 

### BasePageClass

The `BasePage` class contains methods for the most common actions that are expected to be performed on any page. So, 
thinking about our previous selenium script, what actions did we perform? 
```python
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
```

We create this `BaseClass` for two main reasons:
1. All page classes that inherit from the `BaseClass` inherit these methods. 
2. Any update or need to add more common methods will only have to happen to the `BaseClass`

