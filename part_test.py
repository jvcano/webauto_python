import config
from datetime import date
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

curr_date = date.today()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(config.url)
driver.maximize_window()
sleep(1)
driver.find_element(By.NAME,"txtLogin").send_keys(config.username)
#driver.find_element('Name',"txtLogin")
driver.find_element(By.NAME,"txtPassword").send_keys(config.password)
driver.find_element(By.NAME,"btnLogin").click()
sleep(1)
driver.switch_to.frame('aframe')
sleep(1)
#driver.find_element_by_id('inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click()
#var = driver.find_element(By.XPATH,"//table[@id='inbox_inboxoutboxGrid_ctl00']").text
#print(var)
driver.find_element(By.ID,'inbox_inboxoutboxGrid_ctl00_ctl10_hypGetDetails').click() 
sleep(2)
driver.find_element(By.ID,'pnlTimesheet')
sleep(2)
driver.find_element(By.XPATH,"(//div[@id='rptTs_ctl02_ti_rptTI_ctl00_pcParent_dd_parent'])[1]").click()
sleep(2)
driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/a[1]').click()
#print(var)
sleep(2)

driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]").click()
sleep(2)
driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/a[1]').click()
sleep(2)

driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[3]/select[1]').click()