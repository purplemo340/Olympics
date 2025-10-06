from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import numpy as np
import os
# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



#
if os.path.isfile('results/ioc.csv')==True:
    driver.get("https://www.olympics.com/en/news/paris-2024-olympics-full-list-ioc-national-olympic-committee-codes")
    #select=driver.find_element(By.CLASS_NAME, 'sc-370dcec6-0').click()
    
    iocs=driver.find_elements(By.CLASS_NAME, "text-block>p")
    abvs=[]
    for ioc in iocs:
        text=str(ioc.text)
        if '-' in text:
            text=text.strip()
            abv=text.split('-')
            abv[0]=abv[0].strip()
            abv[1]=abv[1].strip()
            abvs.append(abv)
    df=pd.DataFrame(abvs, columns=['Countries', 'Abbreviations', 'drop'])
    df=df.drop('drop', axis=1)
    print(df)
    df.to_csv('results/ioc.csv')     