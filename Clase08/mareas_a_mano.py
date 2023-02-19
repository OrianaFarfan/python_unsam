# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:59:50 2021

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

directorio = '../Data'
archivo = 'OBS_SHN_SF-BA.csv'
path = os.path.join(directorio, archivo)
df = pd.read_csv(path, index_col='Time', parse_dates=True) #Esto explicado en la unidad 

print(df.head())
##Copio un rango de fechas a partir del 25 de diciembre del 2014
dh = df['12-25-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 17.5 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()