# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:07:19 2021

@author: pc
"""

from vigilante import vigilar
import csv
import informe
import formato_tabla


##DEFINO CLASES:
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


#DEFINO FUNCIONES:
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file), types = [str, str, str])
    filas = filtrar_datos (filas, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    while True:
        for fila in filas:
           formateador.fila(fila.values())

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)