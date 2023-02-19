# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:09:00 2021

@author: pc
"""

def ord_burbujeo(lista):
    burb = 1
    aux = 0
    comparaciones = 0

    while burb == 1:
        burb = 0
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                burb = 1
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
            comparaciones += 1

    return comparaciones, lista


#lista_1 = [1, 2, -3, 8, 1, 5]
#print('Comparaciones:',ord_burbujeo(lista_1)[0], 'Lista ordenada:', ord_burbujeo(lista_1)[1])
