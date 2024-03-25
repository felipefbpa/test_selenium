import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://chercher.tech/practice/frames")

#entrando dentro do frame desejado, primeiro mapear ele
iframe1 = browser.find_element(By.ID, "frame1")
#acessar o Iframe
browser.switch_to.frame(iframe1)

txt_input = browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input")
txt_input.send_keys("iframe1")

iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)

checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()

#voltando pra raiz da pagina pois frame2 está ao lado de frame1 e não dentro.
browser.switch_to.default_content()

#entrando dentro do frame desejado, primeiro mapear ele
iframe2 = browser.find_element(By.ID, "frame2")
#acessar o frame
browser.switch_to.frame(iframe2)

#usando Select para selecionar o campo
animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))

#usando seleção por valor dentro do dropdown
animals.select_by_value("babycat")

time.sleep(2)
