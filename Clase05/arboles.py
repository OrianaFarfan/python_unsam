# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:22:59 2021

@author: pc
"""



#Biblioteca y colecciones
import csv
from collections import Counter
#Nuevos Importes
import os
import numpy as np
import matplotlib.pyplot as plt


# Variables
parques = list()
head = list()
canti = Counter()
alturas = list()
maxs = list()
proms = list()
inclinaciones = list()
masincli = list()

#%%
#Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18,
# escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y
# devuelva una lista de diccionarios con la información de todos los árboles
# en el archivo. La función debe devolver una lista conteniendo un diccionario
# por cada árbol con todos los datos.

#Vamos a llamar arboleda a esta lista.

#Funcion leer_arboles

def leer_arboles(nombre_archivo):
    file = open(nombre_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(file)
    Encabezado = next(rows)# Guardo encabezado del archivo como una lista [x,y,z...]

    indices = [Encabezado.index(col) for col in Encabezado] #index() devuelve
                            #la primera aparición / índice del elemento en la lista dada
                            #como argumento de la función.
                            #En este caso recorro la lista de encabezados (for col in Encabezado)
                            #y guardo en la lista indices la posicion (por eso uso index) de cada uno de esos elementos del encabezado
                            #.index(col)=.index(nombre_com) o sea cada nombre del encabezado
                            #Es como decir recorro cada elemento de la lista encabezado y con index le identifico la posicion
  
    arboleda = [{col: row[index] for col, index in zip(Encabezado, indices)} for row in rows]
    #Aca estoy armando una lista con diccionarios [{...}] donde for col,index voy recorriendo la 
    #lista armada con zip con los elementos de la listas Encabezado e indices.
    #Donde col es la clave (Encabezado) y row[index] es el valor (referido al elemento del lugar
    #row[0] de la fila). Es que va a ver una fila de tal forma que [nomb,tipo,x,y,z...] y row[0] es el primer elemento
    
    #Asi se va armar un diccionario por row, o fila. Donde cada diccionario va a tener varias claves
    #con valores asociados
    return arboleda
#%%
#-----------------------------------------------------------------------------------------------------------------------

# Funcion leer_parque
#Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista 
#de diccionarios con la información del parque especificado. La función debe devolver, en una 
#lista un diccionario con todos los datos por cada árbol del parque elegido
# (recordá que cada fila del csv es un árbol).

def leer_parque(nombre_archivo, parque):
    # Variables 
    espacio = list() # Creo la lista para guardar todos los datos
    greenday = list() # Creo la lista con diccionario objetivo
    
    # Abro archivo 'nombre_archivo'
    file = open(nombre_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(file)
    encabezado = next(rows) # Guardo encabezado del archivo
    
    # Leo el resto de las lineas, ya salteado el encabezado
    for row in rows:
        green = dict(zip(encabezado, row)) #armo un diccionario asociando el encabezado con el dato
        espacio.append(green) #lo agrego a la lista
        
        if green["espacio_ve"] == parque: #en el archivo espacio_ve tiene el nombre del parque
        #si green, el diccionario, contiene en espacio verde el nombre del parque que se solicita con ==
            greenday.append(green) #agregamos ese diccionario a otra lista 
    

    file.close() #Acordate de cerrar
    

    return (greenday) #devuelvo la lsita con los diccionarios seleccionados

#---------------------------------------------------------------------------------------------

# Funcion especies

def especies(lista_arboles):
    # Variables internas
    violeta = list() # Lista para adquirir las especies de arboles
    lila = list () # Lista con posibles especies duplicadas
    
    #itero sobre la lista
    for TipoPlanta in lista_arboles: #claro aca tengo greenday que es una lista de diccionario, voy a ir recorriendo 
                                                #cada diccionario de la lista
        lila.append(TipoPlanta["nombre_com"]) # Agrego a una lista todas las especies de plantas en el parque
                            #Aca estoy seleccionando la palabra clave  "nombre_com" de cada diccionario recorrido
                                                            #de la lista
    #con lila armo una lista [x,y,z] de todas las especie
    violeta = set(lila) # Elimino duplicados de lila
    
    
    return (violeta)

#---------------------------------------------------------------------------------------------

# Funcion contar_ejemplares
def contar_ejemplares(lista_arboles):

    ContEspec = Counter() 
    
    #itero sobre la lista
    for cantidad in lista_arboles: #Recorro la lista de diccionarios, cada elemento es informacion de un arbol especifico
        ContEspec[cantidad['nombre_com']] += 1 #sumo uno cada vez que encuentro un arbol del mismo nombre
        
    
    return (ContEspec)

#---------------------------------------------------------------------------------------------


# Funcion obtener_alturas
def obtener_alturas(lista_arboles, especie):
    
    queso = list() # Inicializo una lista de alturas de la especie
    
    for planta in lista_arboles: #Recorre cada elemento (diccionario) de la lista
        if planta['nombre_com'] == especie: #si la especie ingresada coincide con el valor de la clave "nombre_com"
            queso.append(float(planta['altura_tot'])) #agregro el valor de la clave altura_tot  a la lista inicializada
    
    # Retorno con informacion requerida
    return (queso)

#---------------------------------------------------------------------------------------------


#Funcion obtener_inclinaciones
def obtener_inclinaciones(lista_arboles, especie):

    inclinaciones = list() #Inicializo una lista de inclinaciones de la especie
    
    for planta in lista_arboles: #Recorre cada elemento (diccionario) de la lista
        if planta['nombre_com'] == especie: #si la especie ingresada coincide con el valor de la clave "nombre_com"
            inclinaciones.append(float(planta['inclinacio'])) #armo la lista con las inclinaciones segun la especie
    
        return (inclinaciones)

#---------------------------------------------------------------------------------------------

# Funcion especimen_mas_inclinado
def especimen_mas_inclinado(lista_arboles):
    
    MasInclin = list() # Inicializo una lista para guardar especie e inclincacion
    referencia = 0 # Referencia inicial para la inclinacion
    
    for planta in lista_arboles:  #Recorre cada elemento (diccionario) de la lista
        if referencia <= float(planta['inclinacio']): #valor inclinacion mayor a 0
            referencia = float(planta['inclinacio'])
            especie = planta['nombre_com']
            MasInclin = [especie, referencia]


    return (MasInclin)

#----------------------------------------------------------------------------------------------

# Funcion especie_promedio_mas_inclinada
def especie_promedio_mas_inclinada(lista_arboles):

    PlanIncli = list()  # Inicializo una lista para guardar inclincacion
    especimens = list() # Inicizalizo lista de especies
    
    especimens = especies(lista_arboles) #uso la funcion de especies que me da una lista
                                    # de todas las especimens sin repetir
    for especie in especimens: #Recorro la lista de especimens
        incli = obtener_inclinaciones(lista_arboles, especie) #uso la funcion para
                                #obtener las inclinaciones de todas las especimens
                                #que esten en la lista de "especimens"
                                #incli es una funcion que me devuelve una lista
        PlanIncli.append(round(sum(incli)/float(len(incli)),2)) #Sumo todos los
                                        #valores de la lista incli y hago un promedio
                                        #dividiendo segun el largo de la lista incli
    MasIncliP = dict(zip(especimens, PlanIncli)) #Hago una lista con diccionarios que
                                       #contiene el especimen como clave y su inclinacion prom
    

    return (MasIncliP)

#----------------------------------------------------------------------------------------------
# print("Ingresa 3 parques:")
# for n in range(3):
#     park = input(f'Ingrese nombre del parque {n+1}: ') # Ingreso parque
#     head.append(park) # Agrego parque seleccionado en una lista que inicialice al principio
# for x in range(3):
#     #leo la informacion sobre cada parque
#     Parkk = leer_parque('Data/arbolado-en-espacios-verdes.csv', head[x]) 
    
    #obtengo las especies en el parque

#arbolito = input ("Ingrese especie de arbol para analizar: ")


head = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO'] 
arbolito = 'Jacarandá'
#   especie = especies(Parkk)
for x in range(3):
    # Leo informacion sobre cada parque
    Parkk = leer_parque('Data/arbolado-en-espacios-verdes.csv', head[x])
    
    #obtengo la cantidad de especies y las 5 mas frecuentes. Luego guardo las cantidades en una lista
    canti = contar_ejemplares(Parkk)
    frecuentes = canti.most_common(5)
    parques.append(canti)
    
    #obtengo alturas de una especie en los parques, hago promedio y averiguo
    #el arbol mas alto en cada uno
    altura = obtener_alturas(Parkk, arbolito)
    maximo = max(altura)
    maxs.append(maximo)
    promedio = round(sum(altura)/float(len(altura)),3)
    proms.append(promedio)
    
    #obtengo las inclinaciones de los arboles
    inclinaciones.append(obtener_inclinaciones(Parkk, arbolito))
    
    # Averiguo especie mas inclinada
    masinclin = especimen_mas_inclinado(Parkk)
    
    #averiguo la especie que en promedio es la mas inclinada en c/parque
    masincli = especie_promedio_mas_inclinada(Parkk)

#-----------------------------------------------------------------------------------------------------------------------------------
#Clase 4:
#Leo el archivo csv y obtengo información de la variable arboleda en ciudad:
arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')
# Obtengo lista de tuplas con alturas y diametros de una especie
#Alto_Diametro = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == arbolito]
#print(Alto_Diametro)

#Estamos armando una lista con valores float de los valores de la clave "altura_tot"
#de cada diccionario de aboleada. arboleada era una lista que contenida diccionarios
#vamos recorriendo cada fila:
Altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == arbolito]

#Armo un array con la lista de altos y diametros
Alto_Diametro = np.array([(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == arbolito]) # 3.20


# -------------------------------*------------------------------
DataEspecies={}
especiess = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
for especie in especiess:
    alturas=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    diametro=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especie]
    DataEspecies[especie] = (alturas, diametro)

#print(DataEspecies[especies[0]][0]) # Para testear
# -------------------------------*------------------------------

# --------------------------Clase 5-----------------------------------------------
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')

plt.hist(Altos,bins=100) #definido arriba
plt.title("Histograma sobre alturas de Jacarandás de ciudad")

plt.figure()
#En ALto esta array([altura],[diametro])
#significa toda las filas (:) y la segunda columna (1) para x
#significa toda las filas (:) y la primer columna (0)para y
plt.scatter(Alto_Diametro[:,1], Alto_Diametro[:,0], c=np.random.rand(len(Alto_Diametro)), alpha=0.5)
plt.xlabel("Diametro [cm]")
plt.ylabel("Alto [m]")
plt.title("Relación diámetro-alto para Jacarandás")

plt.figure()