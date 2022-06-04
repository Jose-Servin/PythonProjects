from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

base_url = 'https://www.amazon.com/'

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

# TERMINAL COMMAND USED TO ALLOW CHROME DRIVER xattr -d com.apple.quarantine <PATH TO DRIVER>
# driver.close()
