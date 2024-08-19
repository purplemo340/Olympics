from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


columns= ['country', 'gold', 'silver', 'bronze', 'total']
data = [['United States of America', 80, 85, 83, 248], ['Germany', 5,4,5,14], ['Canada', 4,1,1,6], ['Cuba', 3,0,0,3], ["Hungary", 2,1,1,4],['Great Britain', 1,1,0,2], ['Greece', 1,0,1,2], ['Mixed Team', 1,0,0,1]]
countries=np.array(data)
games=countries.tolist()
countries=pd.DataFrame(games, columns=columns)
countries.to_csv(f"results/st-louis-1904.csv")

