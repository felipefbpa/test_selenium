import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://ge.globo.com/rs/futebol/times/gremio/")

menu = browser.find_element(By.XPATH, "//div[@class='menu-button'][1]")
menu.click()

brasileirao = browser.find_element(By.XPATH, "//span[@class='menu-item-title'][1]")
brasileirao.click()

time.sleep(3)