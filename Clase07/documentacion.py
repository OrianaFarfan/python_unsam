# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:07:57 2021

@author: pc
"""

def valor_absoluto(n):
    '''
    Devuelve valor absoluto de n => f(n) = |n|
    ---------------
    Precondicion: valor n real
    Poscondicion: valor n positivo
    '''
    if n >= 0:
        return n
    else:
        return -n

#----------------------------------------------------------------------

def suma_pares(l):
    '''
    Devuelve la suma de numeros pares de una lista
    ---------------
    Pre: valores reales en la lista
    Pos: si el elemento es par: se hace la suma res += e
                  si el elemento es impar: sumo 0
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    # La invariante es que res debe comenzar en 0 para sumar

#----------------------------------------------------------------------

def veces(a, b):
    '''
    Realizo la multiplicacion entre a y b
    ------------
    Pre: valor a real, valor b entero
    Pos: producto entre a y b
    '''
    res = 0 # La invariante es que res debe comenzar en 0 para sumar
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    

#----------------------------------------------------------------------

def collatz(n):
    '''
    Funcion de conjetura de Collatz
    ------------
    Pre: valor n entero positivo
    Pos: si el n es par, se divide entre 2
        si el n es impar, devuelve 3*n+1
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
    # La invariante es que res debe empezar en 1 si el usuario coloca un n = 1