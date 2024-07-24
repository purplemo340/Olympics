import matplotlib.pyplot as plt
from medals import games, countries, type1
import numpy as np
import pandas as pd
x=0
game_info=pd.read_csv('results/games.csv')

for game in games:

    if len(game)<=30:
        fig, ax = plt.subplots(figsize=(10, 10))
        bars=ax.barh(game['country'], game['total'], color=['#30BCED', '#F0E40E'])
        plt.subplots_adjust(left=.3)
        labels = ax.get_xticklabels()
        print(len(game))
        plt.setp(labels, horizontalalignment='right')

        ax.set( xlabel='Medals', ylabel='Countries')
           #title=f"{type1[x].title()} Olympics: {countries[x].title().replace("-", ' ')}")
        ax.bar_label(bars, labels=[f'{medal}' for medal in game['total']])
        fig.set_facecolor('#7BC950')
        plt.savefig(f'static/images/{countries[x].title()}')
        plt.show(block=False)
    else:
        fig, ax1 = plt.subplots( figsize=(10, 16))
        bars=ax1.barh(game['country'], game['total'], color=['#30BCED', '#F0E40E'])
        ax1.set( xlabel='Medals', ylabel='Countries')
                #title=f"{type1[x].title()} Olympics:{countries[x].title().replace("-", ' ')}")
        ax.bar_label(bars, labels=[f'{medal}' for medal in game['total']])
        fig.set_facecolor('#7BC950')
        plt.subplots_adjust(left=.3)
        plt.savefig(f'static/images/{countries[x].title()}')
        plt.show(block=False)

    x+=1