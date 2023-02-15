import config
import calendar
from datetime import date
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


curr_date = date.today()
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument("window-size=1980x960")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.implicitly_wait(5)
driver.get(config.url)
today_date = calendar.day_name[curr_date.weekday()]

driver.find_element(By.NAME,"txtLogin").send_keys(config.username)
driver.find_element(By.NAME,"txtPassword").send_keys(config.password)
driver.find_element(By.NAME,"btnLogin").click()

#!monday 
if today_date == "Monday":
    #sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'menuup_buttonBar_item_2').click()
    #sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl03$ti$rptTI$ctl01$teDet$teVal').send_keys('8')
    #sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    #sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** tuesday
elif today_date == "Tuesday":
    #sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click() #
    #sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl02$teDet$teVal').send_keys('8') #
    #sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    #sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** Wednesday 
elif today_date == "Wednesday":
    #sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
    #sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl03$teDet$teVal').send_keys('8')
    #sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    #sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#***** Thursday 
elif today_date == "Thursday":

    #sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
    #sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl04$teDet$teVal').send_keys('8')
    #sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl03_lb').click()
    #sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
#!friday 
elif today_date == "Friday":

    #sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click() #inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails
    #sleep(2)
    driver.find_element(By.ID,'pnlTimesheet')
    driver.find_element(By.NAME,'rptTs$ctl01$ti$rptTI$ctl05$teDet$teVal').send_keys('8')
    #sleep(2)
    driver.find_element(By.ID,'workflowRoute_ctl07_lb').click()
    #sleep(2)
    driver.get_screenshot_as_file(f'{today_date}.png')
print("done")