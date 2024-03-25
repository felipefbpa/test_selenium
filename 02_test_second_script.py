import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://demo.applitools.com/")

#atribuindo variaveis aos campos
username = browser.find_element(By.ID, "username")
checkbox_remember = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#clicando no checkbox
checkbox_remember.click()

time.sleep(5)

