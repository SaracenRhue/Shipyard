from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

URL = 'http://192.168.178.132/Apps'
TEMPLATE = f'{URL}/AddContainer?xmlTemplate=default:'

driver = webdriver.Firefox()
driver.get(URL)
sleep(1)

# Login
inputs = driver.find_elements(By.TAG_NAME, "input")
inputs[0].send_keys("root")
inputs[1].send_keys("Bazinga!73")
driver.find_element(By.TAG_NAME, "button").click()

driver.get(URL)
sleep(1)
driver.find_element(By.CLASS_NAME, "homeMore").click()
sleep(1)

containers = []
for i in range(1, 2):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    container_links = soup.find_all("div", class_="ca_holder spotlightHome ca_appPopup")
    container_links = [TEMPLATE+l.get("data-apppath") for l in container_links]
    containers.extend(container_links)
    driver.execute_script(f'changePage("{i}")')

print(containers)
driver.execute_script("popupInstallXML('/tmp/community.applications/tempFiles/templates-community-apps/GrafGenixsRepository/androidseb25-iGotify-latest.xml','default','','')")