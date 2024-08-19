from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import numpy as np
import os

games=[]
if os.path.isfile(f"results/paris-2024.csv")==True:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    #driver = webdriver.Chrome(options=chrome_options)
    # Create Chromeoptions instance
    options = webdriver.ChromeOptions()

    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Turn-off userAutomationExtension
    options.add_experimental_option("useAutomationExtension", False)

    # Setting the driver path and requesting a page
    driver = webdriver.Chrome(options=options)

    # Changing the property of the navigator value for webdriver to undefined
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # open website
    columns=["country", "gold", "silver", "bronze", "total"]

    olympic = []


    driver.get("https://web.archive.org/web/20240818203845/https://olympics.com/en/paris-2024/medals")
    games=driver.find_elements(By.CLASS_NAME, 'emotion-srm-fm15hs')
    print(len(games))
    for game in games:

        print(game.text)
        game.text.replace("-", '0')
        result = re.split('\n', game.text)
        olympic.append(result)

    countries=np.array(olympic)

    games=countries.tolist()
    countries=pd.DataFrame(games, columns=columns)

    countries.to_csv(f"results/paris-2024.csv")
    driver.quit()