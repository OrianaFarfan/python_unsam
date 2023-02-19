# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:57:45 2021

@author: pc
"""


# Importo biblioteca y colecciones
import csv
from collections import Counter

# Variables
parques = list()
head = list()
canti = Counter()
alturas = list()
maxs = list()
proms = list()
inclinaciones = list()
masincli = list()

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
print("Ingresa 3 parques:")
for n in range(3):
    park = input(f'Ingrese nombre del parque {n+1}: ') # Ingreso parque
    head.append(park) # Agrego parque seleccionado en una lista que inicialice al principio

arbolito = input ("Ingrese especie de arbol para analizar: ")

for x in range(3):
    #leo la informacion sobre cada parque
    Parkk = leer_parque('Data/arbolado-en-espacios-verdes.csv', head[x]) 
    
    #obtengo las especies en el parque
    especie = especies(Parkk)
    
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
    

   