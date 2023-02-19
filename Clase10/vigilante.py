# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:00:16 2021

@author: pc
"""


import os
import time


def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF: End Of File (fin de archivo)

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        else:
            yield line
        


if __name__ == '__main__':
    import informe

    camion = informe.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')