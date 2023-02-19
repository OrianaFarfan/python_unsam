# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 02:40:09 2021

@author: pc
"""


import warnings
warnings.filterwarnings("ignore")

# Datos a saber del ejercicio:
# 1) Álbum con 670 figuritas.--
# 2) Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
# 3) Cada paquete trae cinco figuritas.

# Importamos:
import random
import numpy as np
import matplotlib.pyplot as plt

# Mis variables:
figus_total = 670 # Cantidad de figuritas en album
figus_paquete = 5 # Cantidad de figuritas en paquete
n_repeticiones = 100 # Veces para analizar llenado de album
paquete = [] # Lista para paquete de figuritas


# Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío 
#con figus_total espacios para pegar figuritas.
def crear_album(figus_total):
    album_make = np.zeros(figus_total, dtype=np.int64) #Aca estoy creando un array de ceros. De tipo int.
    return (album_make)


#Implementá la función album_incompleto(A) que recibe un vector y devuelve True 
#si el álbum A no está completo y False si está completo.
def album_incompleto(A): #Aca estoy recibiendo un A que es un vector de un album, tengo que ver si hay ceros.
    B = A.copy() # Copio la lista para no modificar el original
    B = np.sort(B) # Ordeno de menor a mayor la cantidad de cada figurita
    if B[0] == 0: #Si el menor numero es un cero, o sea que hay un lugar vacio del album.
        return True # Devuelvo True si faltan figuras en el album
    return False # Devuelvo False si esta completo el album



#Implementá una función comprar_figu(figus_total) que reciba el número total de 
#figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un 
#número entero aleatorio que representa la figurita que nos tocó.
def comprar_figu(figus_total):
    figu = random.randint(1,figus_total) #Me devuelve un numero aleatorio random de la figu que nos toco 
    return figu




#Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total),
# genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se 
#debieron comprar para completarlo.

def cuantas_figus(figus_total):
    cant_compras = 0
    album = crear_album(figus_total) # Creo album con la cantidad de figus_totales vacios.
    while album_incompleto(album) == True: #Mientras que tengamos un true, que era que faltaban
        compra = comprar_figu(figus_total) #Elegimos una figu random de las figus_totales
        cant_compras += 1 #Sumamos la cantidad de figus compradas cada vez que pasamos por esta parte
        album[compra-1] += 1 #En el lugar de compra (-1 porque las listas empiezan en cero) se coloca un 1.
    return cant_compras 

cuantas_figus(6)



#Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6
# y guardá en una lista los resultados obtenidos en cada repetición.

figus_total=6
n_repeticiones=1000
l=[]

for i in range(n_repeticiones): #Repetimos 10000 veces la funcion cuantas_figus
    l.append(cuantas_figus(figus_total)) #Agregamos a una lista la cantidad de veces que se tiene 
                                            #que repetir para completar el album si el album tiene 
                                            #un total de figus_total
                
print(f'Para llenar un album de {figus_total} figus compre en promedio {np.mean(l)} figus ({n_repeticiones} repeticiones)')

#Ahora para 670 figus y 100 repeticiones

figus_total=670
n_repeticiones=100
def experimento_figus(n_repeticiones, figus_total):
    l=[]
    for i in range(n_repeticiones): #Repetimos 100 veces la funcion cuantas_figus
        l.append(cuantas_figus(figus_total)) #Agregamos a una lista la cantidad de veces que se tiene 
                                            #que repetir para completar el album si el album tiene 
                                            #un total de figus_total
    return l

print(f'Para llenar un album de {figus_total} figus compre en promedio {np.mean(l)} figus ({n_repeticiones} repeticiones)')



#Ahora en paquetes:
#Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño 
#del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), 
#genere un paquete (lista) de figuritas al azar.
def comprar_paquete(figus_total, figus_paquete):
    pack = np.array([0]*figus_paquete) # Genero vector para 5 figuritas (para llenar por eso 0)
    for i in range(figus_paquete-1): # Genero 5 figuritas aleatorias (va de 0 a 4, pero son 5 for)
        pack[i] = random.randint(1,figus_total)
    return pack

figus_total=670
figus_paquete=5
comprar_paquete(figus_total, figus_paquete)


#Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado 
#el tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, 
#simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
def cuantos_paquetes(figus_total, figus_paquete):
    cant_compras = 0
    album = crear_album(figus_total) # Creo album con un array de largo figus_total
    while album_incompleto(album) == True: #Mientras el album este incompleto
        paquete = comprar_paquete(figus_total, figus_paquete) #Compro paquete de 5 figuritas, que son 5 numeros random
                                                                    #entre 1 y figus_total
        cant_compras += 1 #compra de paquetes
        for i in range(figus_paquete-1): #Por la cantidad de veces de cantidad de figuritas
            album[paquete[i]-1] += 1 #El album en el lugar paquete (-1) coloca un 1, paquete va a ser
                                            # el numero de figurita que obtengo
    return cant_compras

#Hacemos experimentos:
figus_total=670
n_repeticiones=1000
figus_paquete=5

l=[]
for i in range(n_repeticiones): #Repetimos 100 veces la funcion cuantas_figus
    l.append(cuantos_paquetes(figus_total, figus paquete) 