42# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 20:06:08 2021

@author: pc
"""
#En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py 
#que le pida al usuario que ingrese por teclado el radio r de una esfera y 
#calcule e imprima el volumen de la misma. 
#Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

#Finalmente, ejecutá el programa desde la línea de comandos para responder
#¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603

import math #Incluyo libreria math
pi = math.pi # Guardo en una variable el valor pi

print('Ingrese radio de esfera:', end=' ')
r = float(input()) # Pido al usuario que ingrese el radio y lo convierto en float (con decimal)
volumen = (4/3)*pi*(r**3) # Calculo de volumen
print('Volumen de esfera:', round(volumen,4)) # Imprimo en pantalla con cuatro decimales

#print('Volumen de esfera:',volumen) --> es exacto lo que pide.