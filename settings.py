from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

STATE = "TAMIL NADU"
CITY = "CHENNAI"
START_YEAR = "2023"
START_MONTH = "Jan"
START_DAY = "5"
END_YEAR = "2023"
END_MONTH = "Feb"
END_DAY = "5"

def assign(driver): 

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Search by Consignee Location")))
    element.click()

    element = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/select[1]"))
    element.select_by_visible_text(STATE)

    element = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[1]/div[3]/select[1]"))
    element.select_by_visible_text(CITY)

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]")))
    element.click()

    element = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
    element.select_by_visible_text(START_MONTH)

    element = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
    element.select_by_visible_text(START_YEAR)

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, START_DAY)))
    element.click()

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[3]/div[1]/input[1]")))
    element.click()

    element = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
    element.select_by_visible_text(END_MONTH)

    element = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
    element.select_by_visible_text(END_YEAR)

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, END_DAY)))
    element.click()

    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/div[1]/a[1]")))
    element.click()