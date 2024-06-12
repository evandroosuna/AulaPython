from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.globo.com")
driver.implicitly_wait(30) # seconds