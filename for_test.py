import config
import calendar
import holidays
from datetime import date
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

curr_date = date.today()
today_date = calendar.day_name[curr_date.weekday()]
US_holidays = holidays.US()
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument("window-size=1980x960")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get(config.url)
driver.maximize_window()
sleep(1)
driver.find_element(By.NAME,"txtLogin").send_keys(config.username)
#driver.find_element('Name',"txtLogin")
driver.find_element(By.NAME,"txtPassword").send_keys(config.password)
driver.find_element(By.NAME,"btnLogin").click()
sleep(1)
driver.switch_to.frame('aframe')
sleep(2)
