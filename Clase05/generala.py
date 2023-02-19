# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:09:37 2021

@author: pc
"""

from collections import Counter
import random

cant_dados=5
def tirar(cant_dados):
    # tirada = []
    # for i in range(5):
    #     tirada.append(random.randint(1,6))
    #     print(tirada)
    tirada=[random.randint(1,6) for _ in range(cant_dados)]
    return tirada


def generala_no_servida(tirada):
    coun = Counter(tirada)
    (rep,cant) = coun.most_common(1)[0]           #Guardo el num más repetido y cuantas veces salió 
                                                    #Sin ese [0] nos devuelve una lista, como lo tenemos
                                                    #nos da (numrep,cant)
    mesa = [rep]*cant                             #Los dados que quedan en la mesa

    for x in range(2):                            #Se hacen dos nuevas tiradas  (en total son 3)
        for i in range(5-cant):                     #Se hacen con la cantidad de dados - los que tienen valor
                                                    #repetido
            a = random.randint(1,6)                 #Se tiran los dados que nos dan un valor random int entre 1 y 6

            if a == rep:                            #Si en esas dos tiradas se obtiene que los valores son iguales 
                                                    #a los de la rep
                mesa.append(a)                      #lo dejo en la mesa (agrego a la lista)
                cant += 1                           #Se suma en cant

    #print(mesa)

    if len(mesa) == 5:                              #Si al final el largo de mesa es 5, o sea todos los dados
        #print(True)
        return True                                 #Es valor 1
    else:
        return False                                #Es valor 0


N = 1000
G = sum(generala_no_servida(tirar(cant_dados)) for i in range(N))
prob = G/N

print(f'Cantidad de veces que salió generala fue de {G} para {N} tiradas')
print(f'La probabilidad de que salga generala es de: {prob:.5f}')    
