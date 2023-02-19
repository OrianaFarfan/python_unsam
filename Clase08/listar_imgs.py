# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:03:06 2021

@author: pc
"""

# Importamos biblioteca
import os
import pprint
import sys


# Funcion archivos_png
def archivos_png(ruta):
    '''
    Recorro directorio y detecto imagenes *.png
    '''
    archivos = []   # Lista que va a contener ubicaciones de imagenes

    for root, dirs, files in os.walk(ruta): # Recorro ruta
        for name in files:
            archivo = os.path.join(root, name)
            if str(archivo)[-3:] == 'png': #Ultimas 3 palabras del archivo sean png
                archivos.append(archivo)

    pprint.pprint(archivos)


#---------------------------------------------------------#
def main(directorio):
    '''
    Funcion principal
    '''
    archivos_png(directorio)


# _______________________sys________________
if __name__ == '__main__':
    try:
        if len(sys.argv) == 2: # Si paso dos argumentos, lo guardo
            ruta = sys.argv[1]
        else:
            ruta = '.\Data' # Si no, entro por default al asignado
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    main(ruta)