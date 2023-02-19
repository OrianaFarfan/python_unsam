# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:19:26 2021

@author: pc
"""

#Escribí una función llamada propagar que reciba
# un vector con 0's, 1's y -1's y devuelva un vector en el que 
#los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo
# propaga.py.


#Funcion invertir lista
def invertir_lista(lista):
    ListaInvertid = []
    N = len(lista)
    
    for i in range(N-1,-1,-1):
        l = lista[i]
        ListaInvertid.append(l)
    return ListaInvertid


#Funcion de propargar fosforos
def propagar (fosforos):
    #Definimos 2 listas
    fosforosN1 = []
    fosforosN2 = []
    fosfEncend = 0 # Uso fosfEncend para detectar fosforos encendidos
    N = len(fosforos) # Se toma la longitud de los fosforos
    
    
    #Se recorre lista hacia la derecha
    for i in range(0, N): #Va de 0 a N-1 de 1 en 1. 
        f = fosforos[i] #Recorremos los valores del vector fosforo de 1 en 1
        if f == 1: #Si fosforo encendido --> fosfEncend = 1
            fosfEncend = 1
        if f == -1: #Si fosforo apagado --> fosfEncend = 0 o sea no se puede volver a encender
            fosfEncend = 0
        if (f == 0) and (fosfEncend == 1): #Si fosforo apagado y fosfEncend = 1 (que quedo de antes)
            fosforosN1.append(1) #agrego 1 en el mismo lugar pero diferente lugar lista
        else: #O sea si f==0 y fosfEncend = 0 
            fosforosN1.append(f) #se coloca lo mismo que estaba 

    print(fosforosN1)

    #Si se recorre la lista hacia la izquierda
    for i in range(N-1, -1, -1): #como en la funcion invertir
        f = fosforosN1[i] #Empiezo recorriendo los fosfosforos de la lista que me dio
                            #en recorrido anterior y me devolvio fosforosN1
        if f == 1:
            fosfEncend = 1
        if f == -1:
            fosfEncend = 0
        if (f == 0) and (fosfEncend == 1):
            fosforosN2.append(1)
        else:
            fosforosN2.append(f)
    fosforosN2 = invertir_lista(fosforosN2) #invierto la lista para volver a tener
                                                #la original

    return fosforosN2

#fosforosAnt = [0, 0, -1, 0, 1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 0]
fosforosAnt=[ 0, 0, 0, 1, 0, 0]
print(fosforosAnt)

fosforosDesp = propagar(fosforosAnt)
print(fosforosDesp)
