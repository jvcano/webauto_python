import config
from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


curr_date = date.today()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(config.url)
driver.maximize_window()
sleep(3)
driver.find_element(By.NAME,"txtLogin").send_keys(config.username)
#driver.find_element('Name',"txtLogin")
driver.find_element(By.NAME,"txtPassword").send_keys(config.password)
driver.find_element(By.NAME,"btnLogin").click()
sleep(5)
driver.switch_to.frame('aframe')
sleep(1)
driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()