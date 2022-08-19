import config
from datetime import date
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

curr_date = date.today()
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


####################
###holidays and other working 
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
var = driver.find_element((By.XPATH,'/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[3]/select[1]')).text

driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[3]/select[1]').click()
sleep(2)
driver.get_screenshot_as_file(f'saturday.png')























""" var=driver.find_element(By.XPATH,"//a[@id='outbox_inboxoutboxGrid_ctl00_ctl04_hypGetDetails']").text
var3=driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[8]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]").text
var2=driver.find_element(By.XPATH,"//tr[@id='outbox_inboxoutboxGrid_ctl00__0']//td[3]").text
var4=driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[8]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]').text
driver.save_screenshot('Sunday.png') """
#driver.get_screenshot_as_file(f'Sunday.png')
""" 
print(var +" "+ var2 +" "+ var3 +' ' + var4)

file = open("config.py", "a")
var = repr(var)
var2 = repr(var2)      
var3 = repr(var3)
var4 = repr(var4)
file.write("\n" + "date = " +f"{var}" + "\n" +"name = "+f'{var2}' + "\n"+"status = "+f'{var3}'+ "\n"+"hours="+f'{var4}' )
file.close """

