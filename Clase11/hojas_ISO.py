# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 00:11:16 2021

@author: pc
"""

def A(n):
    if n >= 0:
        if n == 0:
            (ancho, largo) = (841, 1189)
            return (ancho, largo)
        else:
            (ancho, largo) = A(n-1)
            
            if ancho > largo:
                ancho = ancho//2
                return (ancho, largo)
            else:
                largo = largo//2
                return (largo, ancho)
    