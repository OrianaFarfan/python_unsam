# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:48:42 2021

@author: pc
"""

class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones
        return self.cajones

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

a = Lote('Manzana', 33, 48.5)
print(a)

# print(a.nombre)
# print(a.precio)
# print(a.cajones)
# print(a.vender(8))
