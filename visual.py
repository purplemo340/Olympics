import matplotlib.pyplot as plt
from medals import list
import numpy as np
import pandas as pd

for game in list:
    df=pd.read_csv(f"results/{game}.csv")
    plt.bar(df['country'],df['total'])
    #plt.legend( loc='best', ncol=4)
    plt.title(f"Olympics:{game}")
    plt.show()