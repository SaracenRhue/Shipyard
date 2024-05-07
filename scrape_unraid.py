from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import requests

URL = 'http://192.168.178.132/Apps'
TEMPLATE = f'{URL}/AddContainer?xmlTemplate=default:'

driver = webdriver.Firefox()
driver.get(URL)
sleep(1)

# Login
per_page = 24
inputs = driver.find_elements(By.TAG_NAME, "input")
inputs[0].send_keys("root")
inputs[1].send_keys("Bazinga!73")
driver.find_element(By.TAG_NAME, "button").click()

for i in range(1,2):
    driver.get(URL)
    sleep(3)
    driver.find_element(By.CLASS_NAME, "homeMore").click()
    sleep(1)
    driver.execute_script(f'changePage("{i}")')


