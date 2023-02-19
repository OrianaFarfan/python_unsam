# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:54:44 2021

@author: pc
"""
# ///---- generala.py ----///


# ACLARACION: Este programa está pensando para tomar los menores valores que más repitan en el primer
# tiro y tomarlo como referencia. Ejemplo:
# Tengo en el primer tiro: [2, 1, 3, 2, 3] <== Tomo 2 de valor 2, tiro 3 dados
# Segundo tiro: [3, 3, 3] <== No hay 2, tiro devuelta
# Tercer tiro: [2, 2, 2] <== Todos son 2, generala! :D


import random
#%%
#Funcion tirar
def tirar():
    return [random.randint(1,6) for _ in range(5)]


#Funcion es_generala tiene que verificar si todos los dados sacan el mismo valor
def es_generala(dados):
   return dados.count(dados[0])==5


n_tiradas=100000
ganadas=sum(es_generala(tirar()) for _ in range(n_tiradas))
#Aca es donde hago un for por la cantidad de tiradas y me voy a fijar
#si es generala cada una de las veces que lo tire con la funcion "es_generala"
#ganadas me va a dar una coleccion de trues (1) o falses (0)
#entonces si lo sumo me da la cantidad de veces que gane.
#Entonces la probabilidad de ganar es:
probabilidad=ganadas/n_tiradas
print(probabilidad)

#%%
#Funcion tirar con un argumento de la cantidad de dados que se quiera:
def tirar(cant_dados):
    return [random.randint(1,6) for _ in range(cant_dados)]


#Funcion es_generala tiene que verificar si todos los dados sacan el mismo valor
def es_generala(dados):
   return dados.count(dados[0])==5


def cuantos_de_cada(dados_en_mesa):
   # return[ (d,dados_en_mesa.count(d)) for d in range(1,6+1) ] #Con esto cuento la cantidad
        #de veces que aparecen los valores del rango del 1 al 6.
   
   # return[ (dados_en_mesa.count(d),d) for d in range(1,6+1) ] #Lo que hice fue cambiar de lugar
        #a la variable d ya que es mas importante la cantidad de veces que se repite y asi voy 
        #a poder utilizar el "sorted" para ordenar de menor a mayor la cantidad de veces.
   
    #Para ordenarlo vamos a usar sorted pero con un parametro de mas para que nos lo ordene de
    #mayor a menor.
    
    return sorted( [ (dados_en_mesa.count(d),d) for d in range(1,6+1) ],
                  reverse=True)



def generala_no_servida():
        manos=3
        mesa=[] #inicialmente no hay ningun dado en la mesa 
        
        for i in range(manos): #Este procedimiento se va a repetir esta cantidad de veces
        
            #Entonces lo primero que tengo que hacer es tirar los dados por lo que en la 
            #mesa van a haber 5 inicialmente. Pero luego se puede decir que en la mesa van a 
            #estar los 5 menos las que voy sacando, que se van guardando en mesa. 
            mesa=mesa+tirar(5-len(mesa)) 
            #la mesa va a ser una lista incialmente vacia. 
            #Luego va a tener valores que voy a guardar mas abajo, que serian los dados repetidos
            #a esos los separo en la lista mesa y los otros los vuelvo a tirar con la funcion 
            
            #lo que se busca es que si en una tirada salen n cantidad de dados de igual valor
            #estos se queden en la mesa, mientras que los otros dados van a seguir tirandose hasta
            #obtener esos valores --> [x,x]+tirar(dadosquequeden)
            
            #Aca tenemos que definir una funcion de "cuantos_de_cada" que esta arriba
             
            if i <manos-1 #o sea no incluyo la ultima mano para esto, sino me quedaria con los de
            #mayor valor
            (cant,valor)=cuantos_de_cada(mesa)[0] #Con ese cero al final nos quedamos con el primer elemento
            #de la lista, ya que cuanto_de_cada me devuelve una lista ordenada tal que [(repetido,valor),(r,v)...]
            #Con ese (cant,valor) ya me armo una tupla
            
        
            #Ahora armo la lista mesa con esos valores que mas se repiten tal que:
            mesa=[valor]*cant
            print(mesa)
        #Entonces al final se obtiene esa lista que va a ir a la funcion es_generala para ver si es o no:
        return es_generala(mesa)
  
  
n_tiradas=10000
ganadas=sum(generala_no_servida() for _ in range(n_tiradas))
#Aca es donde hago un for por la cantidad de tiradas y me voy a fijar
#si es generala cada una de las veces que lo tire con la funcion "es_generala"
#ganadas me va a dar una coleccion de trues (1) o falses (0)
#entonces si lo sumo me da la cantidad de veces que gane.
#Entonces la probabilidad de ganar es:
probabilidad=ganadas/n_tiradas
print(probabilidad)
  
    