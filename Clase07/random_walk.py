# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:19:35 2021

@author: pc
"""

#Importamos bibliotcas 
import numpy as np
import matplotlib.pyplot as plt

# Funciones
def randomwalk(largo):
    pasos = np.random.randint(-1,2,largo) 
    #print(pasos)
    recorrido = pasos.cumsum()   #Sumamos paso a paso los pasos recorridos
    #print(recorrido)
    return recorrido


def desvio(recorridos):

    i_max = 0
    max = 0
    i_min = 0
    min = 0 
    aux = 0 

    distancias = np.absolute(recorridos)
    
    for i, distancia in enumerate(distancias):
        if i == 0: # Tomo de referencia el maximo del primer recorrido
            max = distancia.max()
            min = max
        else:
            aux = distancia.max()
            if aux > max:
                i_max = i
            if aux < min:
                i_min = i

    return (i_min, i_max)


## Valores para implementar la funcion random walk
N = 10000
recorridos = []

plt.figure()
##Ploteo los 12 recorridos
plt.subplot(2, 1, 1)
plt.title('12 random walks')
for i in range(12):
    rw = randomwalk(N)
    recorridos.append(rw)
    plt.plot(rw)
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')

##Obtengo los indices desvios max y min
(i_min, i_max) = desvio(recorridos)

##Ploteo el recorrido con min y max desvio
plt.subplot(2, 2, 3)
plt.plot(recorridos[i_max])
plt.xlabel('Mayor desvío')
plt.subplot(2, 2, 4)
plt.plot(recorridos[i_min])
plt.xlabel('Menor desvío')
plt.show()
