from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
import os
driver = webdriver.Chrome(ChromeDriverManager().install())

class Instabot:
    def  __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        self.driver.get("https://www.youtube.com")
        sleep(2)
        
        search = self.driver.find_element_by_css_selector('input#search')
        search.send_keys("selenium facebook scrapping")
        search.submit()
        sleep(2)


        vid_title = self.driver.find_elements_by_xpath('//a[contains(concat( " ", @class, " " ), concat( " ", "ytd-video-renderer", " " ))]')
        title = []
        for i in range(len(vid_title)):
            title.append(vid_title[i].text)
        data = pd.DataFrame(title)
        #data.dropna(subset=['0'], inplace=True)
        data.columns = ['video titles']
        data.to_excel('C:\\Users\iori_\Documents\webauto_python\output.xlsx',index=False,sheet_name='Youtube names scrapping')
        
        
        new_data = pd.read_excel('C:\\Users\iori_\Documents\webauto_python\output.xlsx')
        new_data.dropna(inplace=True)
        #new_data.set_index('#',inplace=True)
#
        print(new_data)
        new_data.to_excel('C:\\Users\iori_\Documents\webauto_python\output.xlsx',sheet_name='Youtube names scrapping')
#
        os.system(f'start excel.exe ' "C:\\Users\iori_\Documents\webauto_python\output.xlsx")
        sleep(2)

Instabot()