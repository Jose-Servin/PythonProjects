# CREATING A SINGLE POINT OF REFERENCE FOR LOCATORS.
# HELPS WHEN HAVING TO UPDATE AN ELEMENT

from selenium.webdriver.common.by import By


class Locators:
    # --- Home Page Locators ---
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')

    # -- SEARCH RESULT PAGE --
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
