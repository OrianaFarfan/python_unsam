# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:33:04 2021

@author: pc
"""


import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas(nombre_archivo):
    file = np.load(nombre_archivo)           #Para la obtencion de datos
    plt.hist(file,bins=50) #bin es la cantidad de columnas

    plt.title('Temperatura del termometro')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Cantidad de mediciones (n)')

    plt.show()

plotear_temperaturas('..\\Data\\termometro.npy')