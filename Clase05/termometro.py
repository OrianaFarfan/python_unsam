# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:25:21 2021

@author: pc
"""

import random
import numpy as np
from pprint import pprint


def medir_temp(n):

    medicion = []                       #Armo una lista donde voy a gurdar los valores de las mediciones.

    for i in range(n):                #Para un rango de valores entre 0 y n
        medicion.append(37.5+round(random.normalvariate(0, 0.2), 2)) #A la temperatura real (37.5) se le +/- ese valor random
        

    temp_max = max(medicion)            #Busco el maximo entre la lista de medicion
    temp_min = min(medicion)            #Busco el minimo entre la lista de medicion
    prom = round(sum(medicion)/n, 2)            #Hago un promedio de la lista de medicion
    medicion.sort()
    mediana = medicion[round(n/2)]      #Busco el valor central de la medicion. O sea de ntotal busco el nmedio y veo su valor
    valores = [temp_max, temp_min, prom, mediana] #Guardo en una lista

    print(f'Temp max: {valores[0]}°C\nTemp min: {valores[1]}°C\nPromedio: {valores[2]}°C\nMediana: {valores[3]}°C')
   
    return medicion

medicion = medir_temp(999) #Es esa lista de medicion ordenada con sort.

a_medicion = np.array(medicion) #Guardo el vector medicion como un array

np.save('termometro.npy', a_medicion)  #Lo salvo en un archivo

np.savetxt('termometro.csv', a_medicion)
