import config
import calendar
from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


curr_date = date.today()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(config.url)
driver.maximize_window()
today_date = calendar.day_name[curr_date.weekday()]

driver.find_element(By.NAME,"txtLogin").send_keys(config.username)
driver.find_element(By.NAME,"txtPassword").send_keys(config.password)
driver.find_element(By.NAME,"btnLogin").click()

#!monday 
if calendar.day_name[curr_date.weekday()] == "Monday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'menuup_buttonBar_item_2').click()
    sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl01$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** tuesday
elif calendar.day_name[curr_date.weekday()] == "Tuesday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
    sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl02$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** Wednesday 
elif calendar.day_name[curr_date.weekday()] == "Wednesday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
    sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl03$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** Thursday 
elif calendar.day_name[curr_date.weekday()] == "Thursday":

    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
    sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl04$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#!friday 
elif calendar.day_name[curr_date.weekday()] == "Friday":

    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
    sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl05$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl07_lb').click()
    sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
