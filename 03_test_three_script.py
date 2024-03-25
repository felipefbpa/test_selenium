import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.saucedemo.com/")

#atribuindo uma variavel ao campo, encontrando ele pelo ID e XPATH
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.XPATH, "//*[@type='submit']")

#atribuindo o que deve ser inserido no campo
username.send_keys("standard_user")
time.sleep(1)
password.send_keys("secret_sauce")
time.sleep(1)

#clicando em login
btn_login.click()

time.sleep(3)

#mapeando produtos
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(products_title.text)
assert products_title.text == "Products"

#get attribute / XPATH para escolher um de varios elementos colocar o XPATH entre () e a posição do desejado entre []
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")

#para escolher o atributo desejado
print(img_backpack.get_attribute("alt"))