from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# THE KEYS CLASS PROVIDES KEYBOARD KEY VALUES
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.amazon.com/'
search_term = 'Logitech Mechanical Keyboard'

s = Service('/Users/joseservin/PythonProjects/SeleniumBot/drivers/chromedriver')
options = webdriver.ChromeOptions()
# DETACH OPTION ALLOWS CHROMEDRIVER TO STAYS OPEN
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()

# ADDING IMPLICIT WAIT SO SCRIPT DOESN'T ERROR OUT IMMEDIATELY WHEN IT DOESN'T FIND AN ELEMENT ON THE PAGE
driver.implicitly_wait(10)
driver.get(base_url)

# CHECKS WE ARE IN THE CORRECT WEBPAGE (CONNECTION MUST BE SUCCESSFUL FOR THIS TO BE TRUE)
assert "Amazon" in driver.title

# SEARCHING FOR PRODUCT
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
# IT IS BEST PRACTICE CLEARING SEARCH BOXES
search_box.clear()
search_box.send_keys(search_term)
search_box.send_keys(Keys.ENTER)

# to verify if the search results page loaded
assert f"Amazon.com : {search_term}" in driver.title
# to verify if the search results page contains any results or no results were found.
assert "No results found." not in driver.page_source
