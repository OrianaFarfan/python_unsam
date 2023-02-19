# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:39:21 2021

@author: pc
"""

# Importamos bibliotecas
from fileparse import parse_csv
import sys
import gzip

# Funcion leer_camion
def leer_camion(file_name):
    with gzip.open(file_name, 'rt') as file:
        camion = parse_csv(file, types=[str,int,float])
        # Retorno con resultado
        return (camion)

# Funcion leer_precios
def leer_precios(file_name):
    precios = list()
    with open(file_name, 'rt') as file:
        venta = parse_csv(file ,types=[str,float], has_headers=False)
        # Asignacion de header
        header = ['producto', 'venta']
        for tupla in venta:
            venta = dict(zip(header,tupla))
            precios.append(venta)
        
        # Retorno con resultado
        return (precios)

# Funcion hacer_informe
def hacer_informe(camion, precios):
    # Variables
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA['nombre'] == itemB['producto']:
                    producto = itemA['nombre']
                    cantidad = int(itemA['cajones'])
                    precio = round(float(itemA['precio']),2)
                    cambio = round(float(itemB['venta']) - precio, 2)
                    info = (producto, cantidad, precio, cambio)
                    informe.append(info)
            except KeyError:
                continue
    # Retorno con resultado
    return informe

# Funcion imprimir informe:
def imprimir_informe(informe):
    # Variables
    head = ("Producto", "Cajones", "Precio", "Cambio") # Cabecera de informe
    # Impresion
    print(f'{head[0]:^10s}|{head[1]:^10s}|{head[2]:^10s}|{head[3]:^10s}') # Imprimo cabecera
    print("-------------------------------------------") # Linea divisora
    for info in informe: # Genero filas de informe y leo cada por cada for
        info = (info[0], info[1], '$'+str(info[2]), info[3])
        print(f'{info[0]:<10s}|{info[1]:^10d}|{info[2]:^10s}|{info[3]:^10.2f}')
    # Retorno a main
    return

# Funcion informe_camion
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    carga = leer_camion(nombre_archivo_camion) # Leo datos del camion
    chanta = leer_precios(nombre_archivo_precios) # Leo los precios de venta
    informe = hacer_informe(carga, chanta) # Genero un informe
    imprimir_informe(informe) # Imprimo informe en pantalla

# Main
def main(argv):
    if len(sys.argv) != 3:
            raise SystemExit(f'Uso adecuado: {sys.argv[0]}' ' archivo_camion archivo_precios')
    camion = sys.argv[1]
    precios = sys.argv[2]    
    # informe_camion('Data/camion.csv', 'Data/precios.csv')
    informe_camion(camion, precios)


if __name__ == '__main__':
    main(sys.argv)
