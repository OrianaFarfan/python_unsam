# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:07:22 2021

@author: pc
"""

from fileparse import parse_csv # type: ignore


def leer_camion(nombre_archivo):

    camion = parse_csv(nombre_archivo, types=[str,int,float], headers = True)
    #pprint(camion)       
    return camion

def leer_precios(nombre_archivo):
    precios = {}

    precios_lista = parse_csv(nombre_archivo, types=[str,float], headers = False) #Nos devuelve una lista

    for dic in precios_lista: #Recorremos cada diccionario de la lista
        precios.update({dic['Nombre']: dic['Precio']}) #Agregamos al diccionario "precios"
        
    return precios #Devuelvo un diccionario 

def imprimir_informe(camion, precios):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio') #Definimos el header

    print('%10s %10s %10s %10s' % headers) #Con "%" es como que cargamos cada elemento de la tupla "header"

    print('---------- ---------- ---------- ----------')

    for dic in camion: #Recorremos la lista camion que contiene muchos diccionarios [{},{}...]
        if dic != {}: #Si es diferente a un diccionario vacio
            a = dic['nombre'] #Guardamos valor de la clave nombre
            b = dic['cajones'] #Guardamos el valor de la clave cajones
            c = precios[dic['nombre']] #En precios que es un diccionario, busco con la clave "a"
            d = round(float(precios[dic['nombre']])-float(dic['precio']), 2) #Hago la diferencia 
            #entre float precio (que es el diccionario) y el valor float de la lista ("a").
            tupla = (a, b,'$'+str(c), '$'+str(d)) #Guardo variables en una tupla

            print('%10s %10s %10s %10s' % tupla) #Por cada for obtenemos una de estas tuplas impresas
            
    return

def result_final(camion, precios):
    
    costo_camion = 0
    venta = 0

    for dic in camion: #Recorremos cada fila de diccionarios de la lista "camion"
        costo_camion += (int(dic['cajones']) * float(dic['precio'])) #canti cajon * precio del producto
        venta += float(dic['cajones']) * float(precios[dic['nombre']])  #el primero es igual al de antes * el float de ese valor correspondiente a la clave
        #Recordar que "precios" solo tiene clave (nombreproducto) y valor el precio
    print(f'\nEl gasto total fue de ${costo_camion}, la venta total fue de ${venta}')
    print('El monto ganado es de $', round((venta-costo_camion), 2))
    return

def informe_camion(nombre_camion, nombre_precios):
    camion = leer_camion(nombre_camion)
    precios = leer_precios(nombre_precios)
    imprimir_informe(camion, precios)
    result_final(camion, precios)

if __name__ == '__main__':                          
    informe_camion('..\\Data\\camion.csv', '..\\Data\\precios.csv') #necesito esta condicion para que no se ejecuten todas las funciones
                                                                    #cuando importo el modulo
