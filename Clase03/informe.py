# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:41:25 2021

@author: pc
"""
#%%
# Importo biblioteca
import csv

# Variables
total = 0
venta = 0

#%%# Funcion leer_camion
def leer_camion(file_name):
    camion = list() #inicializo una lista
    
    # Abro archivo camion.csv y leo las filas
    file = open(file_name)
    filas = csv.reader(file)
    
    header = next(filas) # Guardo encabezado del archivo y voy a la siguiente fila
    
    # Voy por el resto de lineas
    for line in filas:
        lote = dict(zip(header, line))
        camion.append(lote)
        
   
    file.close()  # Cierro archivo camion.csv!!! importante
    
    return (camion)

#%% # Funcion leer_precios
def leer_precios(file_name):

    venta = list() #inicializo lista

    # Abro archivo precios.csv
    file = open(file_name)
    filas = csv.reader(file)
    
    # Asigno header
    header = ['producto', 'preciob']
    
    
    for line in filas: # Leo contenido del archivo
        try:
            prec = dict(zip(header, line))
            venta.append(prec)
        except IndexError:
            print('No puede interpretar. Fin de analisis de datos\n\n')
    
  
    file.close()   # Cierro archivo precios.csv
    
   
    return (venta)   #Retorno con resultado


#%%

# Carga de archivos en listas de diccionarios
carga = leer_camion('Data/camion.csv')#precios pagados al productor de fruta
verdulero = leer_precios('Data/precios.csv')#precios de verdulero 
#%%
# Balance
for itemA in carga:
    total += int(itemA['cajones']) * float(itemA['precio']) #precio es encabezado de camion.csv
    #lo que hace arriba es obtener el total de cada Ncajon*Precio. De todos los productos
    #es como que busco la clave para que nos de el resultado
    for itemB in verdulero:
        try:
            if itemB['producto'] == itemA['nombre']: #buscamos que el nombre de camion.csv coincida
                                                        #con el producto de precios.cvs (este nombre le puse yo)
                venta += int(itemA['cajones']) * float(itemB['preciob'])
                #multiplicamos el Ncajon por el precio del verdulero
        except KeyError:
            print('Error en la lectura #sad')



print('Final pagado en la descarga del camion: $', total)
print('El costo del camion: $', round(venta-total, 4))
print('Lo que gana el verdulero $', venta)
#%%

