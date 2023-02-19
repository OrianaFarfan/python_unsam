# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 02:27:42 2021

@author: pc
"""

#Construí una función que, a partir de una lista de palabras, 
#devuelva un diccionario geringoso. Las claves del diccionario deben 
#ser las palabras de la lista y los valores deben ser sus traducciones 
#al geringoso (como en el Ejercicio 1.18). 
#Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 

def diccionario_geringoso(lista):
    dic = {} #oara armar un diccionario
    for line in lista:
        row = line.split(',')
        cadena = row[0] #Esto significa que selecciona la primera linea. La cual es la unik
        capadepenapa = '' #empezamos con la variable vacia

        for c in cadena: #Va recorriendo cada caracter de los elementos de la cadena
            capadepenapa = capadepenapa + c
            if c in 'aeiou':
                capadepenapa = capadepenapa + 'p' + c #si la cadena era una aeiou se le 
                                    #suma p y de nuevo la aeiou. ejemplo apa epe ipi y asi
        dic[cadena] = capadepenapa #cadena era cada elemento de la lista. Va a ser nuestra
                            #nueva palabra clave. Esta igualada a su geringoso. Asi se 
                            #arma el diccionario. 

    print(dic)    


diccionario_geringoso(['manzana', 'banana', 'naranja'])