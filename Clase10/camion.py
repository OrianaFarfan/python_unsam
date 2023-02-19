# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:25:45 2021

@author: pc
"""

class Camion:

    def __init__(self, lotes):
        self._lotes = lotes

    def __iter__(self):
        return self._lotes.__iter__()

    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self._lotes])

    def __str__(self):
        return str(self._lotes)

    def __repr__(self):
        return f'Camion({repr(self._lotes)})'

    def precio_total(self):
        '''
        Devuelvo el precio total por lotes en camion
        '''
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        '''
        Devuelvo la cantidad de cajones en los lotes
        '''
        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
