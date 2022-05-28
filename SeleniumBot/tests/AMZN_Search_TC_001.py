from selenium import webdriver

base_url = 'https://www.amazon.com/'

driver = webdriver.Chrome(executable_path='/Users/joseservin/PythonProjects/SeleniumBot/drivers/chromedriver')
driver.maximize_window()

driver.implicitly_wait(10)
driver.get(base_url)

assert "Amazon" in driver.title

driver.close()
