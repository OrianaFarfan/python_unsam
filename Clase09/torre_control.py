# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:48:46 2021

@author: pc
"""

class TorreDeControl():
    '''En base a la clase Cola, se crea una clase TorreDeControl, donde se
    comunica el estado de los aviones que quieren aterrizar y despegar
    '''

    def __init__(self):
        ''' Creo las colas vacias correspondientes'''
        self.lista_ater = []
        self.lista_desp = []

    def nuevo_arribo(self, avion):
        return self.lista_ater.append(avion)

    def nueva_partida(self, avion):
        return self.lista_desp.append(avion)

    def asignar_pista(self):
        if self.lista_ater  != []: #Se ve que no este vacia la lista. Se le asigna a la variable
                                   #"aterrizo" el primer elemento de la lista. Luego se lo libera con pop. 
            self.aterrizo = self.lista_ater[0]
            self.lista_ater.pop(0)
            return f'El vuelo {self.aterrizo} aterrizo con exito'
        elif self.lista_desp != []:
            self.despego = self.lista_desp[0]
            self.lista_desp.pop(0)
            return f'El vuelo {self.despego} despego con exito'
        else:
            return f'No hay vuelos en espera'

    def ver_estado(self):
        if self.lista_ater  != []:
            return f'Vuelos esperando para aterrizar: {self.lista_ater}'  
        if self.lista_desp != []:
            return f'Vuelos esperando para despegar: {self.lista_desp}'


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
print(torre.ver_estado())
print(torre.asignar_pista())
print(torre.asignar_pista())
print(torre.asignar_pista())
print(torre.asignar_pista())


    