from calendar import calendar
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import calendar

curr_date = date.today()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://booking.com/")
driver.maximize_window()

sleep(2)
driver.find_element("name","ss").send_keys("italy")
sleep(2)
#driver.find_element_by_css_selector('button["xp__dates-inner"]').click()
driver.find_element(By.LINK_TEXT,'Flights').click()
#driver.find_elements_by_css_selector('').click()
#driver.find_element_by_css_selector('a[data-modal-header-async-url-param*=""]').click()
driver.get_screenshot_as_file(f'{calendar.day_name[curr_date.weekday()]}''.png')
