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

driver.find_element_by_name("txtLogin").send_keys(config.username)
driver.find_element_by_name("txtPassword").send_keys(config.password)
driver.find_element_by_name("btnLogin").click()

#**monday 
if calendar.day_name[curr_date.weekday()] == "Monday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element_by_id('menuup_buttonBar_item_2').click()
    sleep(2)
    driver.find_element_by_id('pnlTimesheet')
    driver.find_element_by_name('rptTs$ctl01$ti$rptTI$ctl01$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element_by_id('workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file('Monday.png')
#***** tuesday
elif calendar.day_name[curr_date.weekday()] == "Tuesday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
    sleep(2)
    driver.find_element_by_id('pnlTimesheet')
    driver.find_element_by_name('rptTs$ctl01$ti$rptTI$ctl02$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element_by_id('workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file('Tuesday.png')
#***** Wednesday 
elif calendar.day_name[curr_date.weekday()] == "Wednesday":
    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
    sleep(2)
    driver.find_element_by_id('pnlTimesheet')
    driver.find_element_by_name('rptTs$ctl01$ti$rptTI$ctl03$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element_by_id('workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file('Wednesday.png')
#***** Thursday 
elif calendar.day_name[curr_date.weekday()] == "Thursday":

    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
    sleep(2)
    driver.find_element_by_id('pnlTimesheet')
    driver.find_element_by_name('rptTs$ctl01$ti$rptTI$ctl04$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element_by_id('workflowRoute_ctl03_lb').click()
    sleep(2)
    driver.get_screenshot_as_file('Thursday.png')
#!friday 
elif calendar.day_name[curr_date.weekday()] == "Friday":

    sleep(2)
    driver.switch_to.frame('aframe')
    driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl12_hypGetDetails').click()
    sleep(2)
    driver.find_element_by_id('pnlTimesheet')
    driver.find_element_by_name('rptTs$ctl01$ti$rptTI$ctl05$teDet$teVal').send_keys('8')
    sleep(2)
    driver.find_element_by_id('workflowRoute_ctl07_lb').click()
    sleep(2)
    driver.get_screenshot_as_file('Friday.png')







#driver.find_element_by_id('menuup_buttonBar_item_7').click()




#//a[normalize-space()='User Reports']