from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://booking.com/")
driver.maximize_window()

sleep(2)
driver.find_element_by_name("ss").send_keys("italy")
sleep(2)
#driver.find_element_by_css_selector('button["xp__dates-inner"]').click()
driver.find_element_by_link_text('Flights').click()
#driver.find_elements_by_css_selector('').click()
#driver.find_element_by_css_selector('a[data-modal-header-async-url-param*=""]').click()
driver.get_screenshot_as_file('/home/ccentos/timesheet/webauto_python/screenie.png')


