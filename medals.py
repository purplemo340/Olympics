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
if os.path.isfile('results/games.csv')==False:
    driver.get("https://olympics.com/en/olympic-games/olympic-results")
    links=driver.find_elements(By.CLASS_NAME, "sc-eVedOh")
    print(len(links))
    list=[]
    result=[]
    for link in links:
        if len(link.text)>0:
            link=link.text.strip()
            l=link.replace(" ", "-")
            l=l.replace("'", "-") #for cortina d ampezz
            l = l.replace(".", "")

            l=l.lower()
            result=re.split('\n', l)
            #print(l)
            letters=re.findall(r'[a-z.]+', l)
            num=re.findall(r'[0-9]+', l)
            print(result[0])
            list.append(result)
            #print(letters)
    print(result)
    countries=np.array(list)
    countries=countries.reshape(len(countries),2)
    countries=pd.DataFrame(countries, columns=['City-Year', 'Type'])
    countries.to_csv(f"results/games.csv")
    driver.quit()

#
# keep chrome open
past_game=pd.read_csv('results/games.csv')
games=[]
for past in past_game['City-Year']:
    if os.path.isfile(f"results/{past}.csv")==False:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        # open website


        columns=["country", "gold", "silver", "bronze", "total"]

        olympic = []
        driver.get(f"https://olympics.com/en/olympic-games/{past}/medals")

        games=driver.find_elements(By.CSS_SELECTOR, 'div>div>div>span')
        for game in games:
            if game.text!='' and game.text!='Copyright 2024. All rights reserved':
                olympic.append(game.text.replace("-", '0'))
        print(olympic)

        countries=np.array(olympic)
        countries=countries.reshape(int(len(olympic)/5),5)
        games=countries.tolist()
        countries=pd.DataFrame(games, columns=columns)

        countries.to_csv(f"results/{past}.csv")

    games.append(pd.read_csv(f"results/{past}.csv"))

countries=pd.read_csv(f"results/games.csv")['City-Year']
type1=pd.read_csv(f"results/games.csv")['Type']
driver.quit()
