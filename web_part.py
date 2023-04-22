# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import settings

website = 'https://bidplus.gem.gov.in/advance-search'

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(website)
settings.assign(driver)
# driver.quit()