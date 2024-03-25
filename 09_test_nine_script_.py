import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.maximize_window()

browser.get("https://www.saucedemo.com/")

# Fazendo login
username = browser.find_element(By.ID, "user-name").send_keys("standard_user")
password = browser.find_element(By.ID, "password").send_keys("senhaErrada")
btn_login = browser.find_element(By.XPATH, "//*[@type='submit']").click()

# Verificando se o login foi correto conferindo se campo da pagina posterior apareceu
assert browser.find_element(By.XPATH, "//span[@class='title']").is_displayed

time.sleep(2)

