import matplotlib.pyplot as plt
from medals import games, countries, type
import numpy as np
import pandas as pd
x=0
game_info=pd.read_csv('results/games.csv')

for game in games:

    if type[x]=='winter':
        fig, ax = plt.subplots(figsize=(18, 12))
        ax.bar(game['country'], game['total'], color=['turquoise', 'gold'])
        labels = ax.get_xticklabels()
        print(len(game))
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set( xlabel='Countries', ylabel='Medals',
           title=f"Olympics:{countries[x]}")
        plt.show()
    else:
        fig, (ax1,ax2) = plt.subplots(2,1, figsize=(18, 12))
        ax1.bar(game['country'][0:int(len(game)/2)], game['total'][0:int(len(game)/2)], color=['turquoise', 'gold'])
        labels = ax1.get_xticklabels()
        print(len(game))
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax1.set(xlabel='Countries', ylabel='Medals',
               title=f"Olympics:{countries[x]}")
        ax2.bar(game['country'][int(len(game)/2):], game['total'][int(len(game)/2):], color=['turquoise', 'gold'])
        labels = ax2.get_xticklabels()
        ax2.set(xlabel='Countries', ylabel='Medals')
        plt.setp(labels, rotation=45, horizontalalignment='right')

        plt.show()

    x+=1