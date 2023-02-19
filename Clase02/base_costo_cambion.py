# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:43:08 2021

@author: pc
"""

# fragmento de costo_camion.py 
#ESTO LO SUBIERON LOS PROFES
import csv
...

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            total += ncajones * precio
    return total

costo_camion('camion.csv')