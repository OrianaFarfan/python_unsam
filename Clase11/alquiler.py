# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:36:38 2021

@author: pc
"""


import numpy as np
import matplotlib.pyplot as plt


#Funcion dada por el ejercicio:
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


#Variables:
minx = 0
maxx = 200
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])


a, b = ajuste_lineal_simple(superficie, alquiler)

#Armo datos para la tendencia lineal
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

#Para plot:
h = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'g')
plt.xlabel('x')
plt.ylabel('y')

#Error Cuadratico Medio:
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())

#Plot final:
plt.show()