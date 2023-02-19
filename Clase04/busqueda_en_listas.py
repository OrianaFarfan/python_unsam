# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:56:44 2021

@author: pc
"""

#En este primer ejercicio tenés que escribir una función buscar_u_elemento() 
#que reciba una lista y un elemento y devuelva la posición de la última aparición
# de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).

#Ejercicio 4.3 
#Funcion buscar_u_elemento:
    
def buscar_u_elemento(lista, elemente):
    posi = -1 #Inicialmente se considera que elemente no esta en lista
    for i, l in enumerate(lista): #el operador enumerate nos devolvia la    
                #posicion y el elemento asociado a esa posicion. 
                #i es posiciony l es elemento de la posicion i
        if l == elemente: # Si encuentro elemente en lista, obtengo posi y salgo
            posi = i
            break
    return posi


#Funcion buscar_n_elemento 
#Busco la cantidad de veces que aparece un elemento en la lista
def buscar_n_elemento(lista, elemente): 
    v = 0 # Variable inicializada en 0 para contar las veces de ocurrencias
    for l in lista: #Recorremos los elementos de la lista
        if l == elemente: #Si el elemento l de la lista es igual a elemente
            v += 1 #Se cuenta uno 
    return v



#Ejercicio 4.4
#Se busca el maximo en lista (considero que tengo lista de int) 
def maximo(lista): 
    maximo = 0 # variable inicializada en 0
    for i, l in enumerate(lista): #Vamos recorriendo i (posicion) asociada a su
                                        #valor (l)
        if i == 0: #Se toma el primer valor de la lista como referencia
            maximo = int(l) #definimos el valor de esa posicion como el maximo de referencia
        if int(l) > maximo: #Para la proxima ronda si el valor int "l" es mayor a maximo
                            #que se definio en el primer if
            maximo = int(l) #Entonces guardamos ese valor de nuevo en maximo, pisando
                            #al anterior
    return maximo


#Se busca el minimo en lista (considero que tengo lista de int) 
def minimo(lista):
    minimo = 0 # variable inicializada en 0
    for i, l in enumerate(lista):#Vamos recorriendo i (posicion) asociada a su
                                        #valor (l)
        if i == 0: #Se toma el primer valor de la lista como referencia
            minimo = int(l)#definimos el valor de esa posicion como el minimo de referencia
        if int(l) < minimo:#Para la proxima ronda si el valor int "l" es menor a minimo
                            #que se definio en el primer if
            minimo = int(l)#Entonces guardamos ese valor de nuevo en maximo, pisando
                            #al anterior
    return minimo



