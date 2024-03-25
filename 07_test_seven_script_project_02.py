import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.maximize_window()

browser.get("https://www.saucedemo.com/")

# Fazendo login
username = browser.find_element(By.ID, "user-name").send_keys("standard_user")
password = browser.find_element(By.ID, "password").send_keys("secret_sauce")
btn_login = browser.find_element(By.XPATH, "//*[@type='submit']").click()

# Colocando itens no carrinho
browser.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
browser.find_element(By.XPATH, "//*[text()='Add to cart']").click()

# Verificando carrinho
browser.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

# Voltando para a tela de produtos 
browser.find_element(By.ID, "continue-shopping").click()

# Colocando itens no carrinho
browser.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
browser.find_element(By.XPATH, "//*[text()='Add to cart']").click()

# Verificando carrinho
browser.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

time.sleep(2)