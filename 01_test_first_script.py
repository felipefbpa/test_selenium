import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

#atribuindo uma variavel ao campo, encontrando ele pelo ID
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

#atribuindo o que deve ser inserido no campo
username.send_keys("standard_user")
password.send_keys("secret_sauce")

time.sleep(2)