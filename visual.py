import matplotlib.pyplot as plt
from medals import games, countries
import numpy as np
import pandas as pd
x=0
for game in games:
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.barh(game['country'], game['total'])
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    ax.set(xlim=[0, 150], xlabel='Medals>', ylabel='Countries',
           title=f"Olympics:{countries[x]}")
    plt.show()
    # plt.bar(game['country'],game['total'])
    # #plt.legend( loc='best', ncol=4)
    # print(countries[x])
    # plt.title(f"Olympics:{countries[x]}")
    # plt.xticks(rotation=60)
    # plt.ylabel('Medals')
     # plt.show()
    x+=1