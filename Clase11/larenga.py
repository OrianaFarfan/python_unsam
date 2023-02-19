# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:58:07 2021

@author: pc
"""

def pascal(n, k):
    '''
    A partir de n, k >= 0, hallo el valor solicitado
    en el triangulo de Pascal
    n: fila, k: columna
    '''
    if (k == 0) or (n == k): # Caso base
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

print(pascal(5, 2))