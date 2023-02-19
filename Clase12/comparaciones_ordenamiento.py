# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:37:59 2021

@author: pc
"""

import seleccion
import insercion
import burbujeo
import merge_sort
import numpy as np
import matplotlib.pyplot as plt

comp_s = [] #Lista de comps seleccion
comp_i = [] #Lista de comps insercion
comp_b = [] #Lista de comps burbujeo
comp_ms = [] #Lista de comps merge_sort
lista_rd = []

for n in range(256):
    lista_rd.append(np.random.randint(1, 1001)) #Elijo un valor random entre esos extremos
    
    comp_b.append(burbujeo.ord_burbujeo(lista_rd.copy()))
    comp_i.append(insercion.ord_insercion(lista_rd.copy()))
    comp_s.append(seleccion.ord_seleccion(lista_rd.copy()))
    comp_ms.append(merge_sort.merge_sort(lista_rd.copy())[1])
    
y = np.array([comp_b, comp_i, comp_s, comp_ms])
x = np.arange(1, 256+1, 1)


for i in range(4):
    plt.plot(x, y[i])

plt.xlabel('Largo de la lista')
plt.ylabel('Comparaciones')
plt.legend(['Burbujeo', 'Insercion', 'Seleccion', 'Merge_Sort'])
plt.title('Métodos de ordenamiento')

plt.show()