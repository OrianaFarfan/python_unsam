# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 03:40:22 2021

@author: pc
"""

# informe.py


import csv # Importo biblioteca

# Defino variables
total = 0
venta = 0

#%%
# Funcion leer_camion que devuelve una lista de diccionario, antes deberia ser tupla.
def leer_camion(file_name):
    # Variables
    camion = list() #tenés que empezar con una variable que empieza siendo una lista vacía
                #Tambien se podria usar camion = []

    
    # Abro archivo camion.csv
    file = open(file_name)
    rows = csv.reader(file)
    
    header = next(rows) # Guardo cabezera y salto a la siguiente linea
    
    
    for line in rows: # Leo resto de lineas, linea por linea
        lote = dict(zip(header, line)) #  lote = (row[0], int(row[1]), float(row[2]))?
                #Zip hace una lista tal que [(header1,line1),(header2,line2),...]
                #Dict crea un diccionario donde headerX es la clave y lineX es su definicion
        camion.append(lote) #Agrego cada linea a la lista camion. 
       # print(lote) AAVER
   
    file.close() # Cierro archivo camion.csv
    
    # Retorno con resultado
    return (camion)


#%% 
#con respecto a la funcion que busca el precio de una fruta:
#Escribí una función leer_precios(nombre_archivo) que a partir de un
# conjunto de precios como éste arme un diccionario donde las claves 
#sean los nombres de frutas y verduras, y los valores sean los precios por cajón.


# Funcion leer_precios
def leer_precios(file_name): 
    # Variables
    venta = list()   #tenés que empezar con una variable que empieza siendo una lista vacía
                #Tambien se podria usar camion = []

    # Abro archivo precios.csv
    file = open(file_name)
    rows = csv.reader(file)
    
   
    header = ['producto', 'preciob']  # Asigno encabezado porque ese archivo no tenia
        #El archivo tiene 2 columas, x filas. (x,1) o (x,2)
    
    # Leo contenido del archivo
    for line in rows:
        try:
            price = dict(zip(header, line))
            #Zip hace una lista tal que [(header1,line1),(header2,line2),...]
            #creo que seria producto:x billetin:x en una lista. un diccionario con 2 def
            #Dict crea un diccionario donde headerX es la clave y lineX es su definicion
            venta.append(price)
            #print(price) AAVER
        except IndexError:
            print('Fin de analisis de datos\n\n')
    
    # Cierro archivo precios.csv
    file.close()
    
    # Retorno con resultado
    return (venta)

# Carga de archivos en listas de diccionarios
carga = leer_camion('camion.csv') #precios pagados al productor de fruta
verdulero = leer_precios('precios.csv') #precios de verdulero 

# Balance
for itemA in carga:
    total += int(itemA['cajones']) * float(itemA['precio']) #precio es encabezado de camion.csv
    #lo que hace arriba es obtener el total de cada Ncajon*Precio. De todos los productos
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