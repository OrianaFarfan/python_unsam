# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:57:26 2021

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
     #el encabezado tiene [nombre,cajones,precio]
    
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
# Funcion hacer_informe
def hacer_informe(camion, precios):
    
    informe = [] #inicializo una lista
    for itemA in camion: #con esto pasaria a cada elemento de la lista que serian los diccionarios
        for itemB in precios: #lo mismo, pasa por cada diccionario de la lista en donde estan
            try:
                if itemA['nombre'] == itemB['producto']: #solo tomo en cuenta los productos que
                                                        #comparten ambos
                    producto = itemA['nombre']
                    cantidad = int(itemA['cajones'])
                    precio = round(float(itemA['precio']),2)
                    cambio = round(float(itemB['preciob']) - precio, 2) #preciob era de verdulero
                    info = (producto, cantidad, precio, cambio) #tupla
                    informe.append(info) #agregro a la lista la "tupla" info
            except KeyError:
                continue
    # Retorno con resultado
    return informe
#%%
# Carga de archivos en listas de diccionarios y tuplas
carga = leer_camion('Data/camion.csv')
verdulero = leer_precios('Data/precios.csv')
informe = hacer_informe(carga, verdulero)
#%%
# Generacion de tabla
cabeza = ("Producto", "Cajones", "Precio", "Cambio")
print(f'{cabeza[0]:^10s}|{cabeza[1]:^10s}|{cabeza[2]:^10s}|{cabeza[3]:^10s}')
print("-"*40)
for info in informe: #recorro la lista informe que tiene tuplas
    info = (info[0], info[1], '$'+str(info[2]), info[3]) #voy yendo a cada tupla de la lista informe
    print(f'{info[0]:<10s}|{info[1]:^10d}|{info[2]:^10s}|{info[3]:^10.2f}')
    