from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import numpy
# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



#
driver.get("https://olympics.com/en/olympic-games/olympic-results")
links=driver.find_elements(By.CLASS_NAME, "link-item")
print(len(links))
list=[]
for link in links:
    if len(link.text)>0:
        link=link.text.strip()
        l=link.replace(" ", "-")
        l=l.replace("'", "-") #for cortina d ampezz
        l = l.replace(".", "")
        l=l.lower()
        print(l)
        letters=re.findall(r'[a-z.]+', l)
        num=re.findall(r'[0-9]+', l)
        list.append(l)
        print(letters)
driver.quit()

#
# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
# open website
olympic=[]
columns=["country", "gold", "silver", "bronze", "total"]
for past in list[0:len(list)-3]:
    driver.get(f"https://olympics.com/en/olympic-games/{past}/medals")

    games=driver.find_element(By.XPATH, '//*[@id="grid-container"]/div[1]/div[3]')

    games=re.split("\n", games.text)

    countries=numpy.array(games)
    countries=countries.reshape(int(len(games)/5),5)
    games=countries.tolist()
    countries=pd.DataFrame(games, columns=columns)
    olympic.append(countries)
    countries.to_csv(f"results/{past}.csv")


    # for city in cities:
    #     print(city.text)
    # #print(len(countries))


driver.quit()
