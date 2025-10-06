import matplotlib.pyplot as plt
#from medals import games, countries, type1
import numpy as np
import pandas as pd
from time import sleep
x=0
game_info=pd.read_csv('results/games.csv')
countries=game_info["City-Year"]
cities=game_info["City"]
game_info=game_info[game_info['City-Year']=='st-louis-1904']

for games in game_info['City-Year']:
    game=pd.read_csv(f'results/{games}.csv')
    length=int(len(game))
    four=int(length/4)
    two=int(length/2)
    if length<10:
        fig, ax = plt.subplots( figsize=(16,10))
        bars=ax.bar(game['abv'], game['total'], color=['#30BCED', '#F0E40E'])
        ax.set(xlabel='Countries', ylabel='Medals')
        ax.bar_label(bars, labels=[f'{medal}' for medal in game['total']])
    elif length<30:
        
        fig, (ax,ax1) = plt.subplots(2,1, figsize=(16,10))
        bars=ax.bar(game[0:((two))]['abv'], game[0:(two)]['total'], color=['#30BCED', '#F0E40E'])
        ax.set( ylabel='Medals')
        ax.bar_label(bars, labels=[f'{medal}' for medal in game[0:((two))]['total']])


        bars=ax1.bar(game[two:]['abv'], game[two:]['total'], color=['#30BCED', '#F0E40E'])
        ax1.set( xlabel='Countries', ylabel='Medals')
        ax1.bar_label(bars, labels=[f'{medal}' for medal in game[two:]['total']])
    else:
        fig, (ax,ax1,ax2, ax3) = plt.subplots(4,1, figsize=(16,10))
        a=[ax, ax1,ax2, ax3]
        bars=ax.bar(game[0:((four))]['abv'], game[0:((four))]['total'], color=['#30BCED', '#F0E40E'])
        ax.set( ylabel='Medals')
        ax.bar_label(bars, labels=[f'{medal}' for medal in game[0:((four))]['total']])


        bars=ax1.bar(game[four:((four*2))]['abv'], game[four:((four*2))]['total'], color=['#30BCED', '#F0E40E'])
        ax1.set( ylabel='Medals')
        ax1.bar_label(bars, labels=[f'{medal}' for medal in game[four:((four*2))]['total']])


        bars=ax2.bar(game[(four*2):(four*3)]['abv'], game[(four*2):((four*3))]['total'], color=['#30BCED', '#F0E40E'])
        ax2.set( ylabel='Medals')
        ax2.bar_label(bars, labels=[f'{medal}' for medal in game[(four*2):((four*3))]['total']])


        bars=ax3.bar(game[(four*3):]['abv'], game[(four*3):]['total'], color=['#30BCED', '#F0E40E'])
        ax3.set(xlabel='Countries', ylabel='Medals')
        ax3.bar_label(bars, labels=[f'{medal}' for medal in game[(four*3):]['total']])

    fig.set_facecolor('#7BC950')
    plt.subplots_adjust(left=.3)
    fig.tight_layout()
    plt.savefig(f'static/images/{games.title()}')
    plt.show()
    sleep(2)
    plt.close()