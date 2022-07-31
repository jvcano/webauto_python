import config
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(config.url)

driver.find_element_by_name("txtLogin").send_keys(config.username)
driver.find_element_by_name("txtPassword").send_keys(config.password)
driver.find_element_by_name("btnLogin").click()

sleep(5)

#driver.find_element_by_id This element is in iframe - #outbox_inboxoutboxGrid_ctl00_ctl04_hypGetDetails
driver.find_element_by_link_text("Jul 25, 2022").click()

#