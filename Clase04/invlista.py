# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:50:58 2021

@author: pc
"""


#Funcion invertir lista:
    
def invertir_lista(lista):
    ListaInvertid = [] #Creo una lista donde voy a 
                        #tener los elementos en orden invertido
    N = len(lista)      #Mido el largo de la lista
    
    for i in range(N-1,-1,-1): #range(start, stop, step) 
                    #en este caso empieza en N-1, para en 0 (-1) y va de atras 
                    #hacia adelante
                 #esta bien porque la lista empieza de 0 y termina en N-1 si    
                 #tiene N elementos.
        l = lista[i] #Se va a ir recorriendo lo elementos de la lista del 
                    #argumento de atras hacia adelante, segun i
        ListaInvertid.append(l) #Vamos agregando los elementos de la lista a 
                                    #la lista invertida
    return ListaInvertid #Devolvemos la lista



#Probamos:
#listaV = [1,2,3,4,5]
listaI = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
listaF = invertir_lista(listaI)
print (listaF)
