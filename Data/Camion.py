# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:27:47 2021

@author: pc
"""

def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
        print(total)
    return total

#para llamar a la funcion:
a=sumcount(10)    