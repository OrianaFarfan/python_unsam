# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:27:02 2021

@author: pc
"""

# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe',
#'pi', 'po', o 'pu' según corresponda luego de cada vocal.


cadena = 'Geringoso' # Cadena de referencia
capadepenapa = '' # Nombre random geringoso para la cadena para rellenar
for c in cadena:
	if c == 'a':
		capadepenapa = capadepenapa + 'apa'
	elif c == 'e':
		capadepenapa = capadepenapa + 'epe'
	elif c == 'i':
		capadepenapa = capadepenapa + 'ipi'
	elif c == 'o':
		capadepenapa = capadepenapa + 'opo'
	elif c == 'u':
		capadepenapa = capadepenapa + 'upu'
	else:
		capadepenapa = capadepenapa + c #O sea que si en la cadena recorrida "cadena" no hay
                                        #vocales se coloca la letra que estaba, como la G del principio


print(capadepenapa)
