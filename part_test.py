import config
import calendar
from datetime import date
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


curr_date = date.today()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(config.url)
driver.maximize_window()
sleep(3)
driver.find_element_by_name("txtLogin").send_keys(config.username)
driver.find_element_by_name("txtPassword").send_keys(config.password)
driver.find_element_by_name("btnLogin").click()
sleep(2)
driver.switch_to.frame('aframe')
driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
sleep(2)