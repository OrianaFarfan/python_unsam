# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:09:49 2021

@author: pc
"""

from fileparse import parse_csv  
from camion import Camion
from lote import Lote   
import formato_tabla   
import sys


def leer_camion(nombre_archivo):

    camion_dic = parse_csv(nombre_archivo,
                        select=['nombre','cajones','precio'],
                        types=[str,int,float], headers = True)

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dic] #Por cada elemento en
                                                                                #camion_dic, pongo esos valores en la clase lote
    #Me devuelve cada variable definida, no aplique metodo. 
    return Camion(camion)

def leer_precios(nombre_archivo):
    precios = {}

    precios_lista = parse_csv(nombre_archivo, types=[str,float], headers = False)

    for dic in precios_lista:
        precios.update({dic['Nombre']: dic['Precio']})

    return precios


def imprimir_informe(camion, precios, formateador):
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])

    # print('%10s %10s %10s %10s' % headers)

    for dic in camion:
        if dic != {}:
            nombre = dic.nombre
            cajones = dic.cajones
            precio = precios[dic.nombre]
            cambio = round(float(precios[dic.nombre])-float(dic.precio), 3)
            #tupla = (a, b,'$'+str(c), '$'+str(d))

            #print('%10s %10s %10s %10s' % tupla)
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.3f}' ]
        formateador.fila(rowdata)

    return


def result_final(camion, precios):

    costo_camion = 0
    venta = 0

    for dic in camion:
        costo_camion += (int(dic.cajones) * float(dic.precio))
        venta += float(dic.cajones) * float(precios[dic.nombre])

    print(f'\nEl gasto total fue de ${costo_camion} y la venta total fue de ${venta}')
    print('El monto ganado es de $', round((venta-costo_camion), 3))
    return

def informe_camion(nombre_camion, nombre_precios, fmt):
    #Pasar la info de los csv a objetos
    camion = leer_camion(nombre_camion)
    precios = leer_precios(nombre_precios)

    #Imprimir informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(camion, precios, formateador)

    #Calcular gasto, venta y ganancia total
    result_final(camion, precios)

def main(argv):
    if len(argv) == 4:
        camion = sys.argv[1]
        precios = sys.argv[2]
        formato = sys.argv[3]
    else:
        raise SystemExit(f'Cantidad de parametros equivocados')

    informe_camion(camion, precios, formato)

if __name__ == '__main__':
    main(sys.argv)



