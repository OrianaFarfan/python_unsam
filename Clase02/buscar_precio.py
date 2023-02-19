# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 00:31:27 2021

@author: pc
"""

#A partir de lo que hiciste en el Ejercicio 2.3, escribí una 
#función buscar_precio(fruta) que busque en archivo ../Data/precios.csv 
#el precio de determinada fruta (o verdura) y lo imprima en pantalla. 
#Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.


def buscar_precio(producto):
    data = open('precios.csv', 'rt')

    headers = next(data).split(',')

    for line in data:
        row = line.split(',')
        if row[0] == producto: #como que dice si el nombre del producto esta en alguna de
                                #de las columnas de la posicion (1,x)
            print(f'El precio de {producto} es: {row[1]}')
    
     #  elif row[0] != producto:
     #       print('no esta') no entiendo porque no funciona
            

    data.close()


buscar_precio('Durazno')