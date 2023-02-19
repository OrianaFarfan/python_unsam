# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 00:30:51 2021

@author: pc
"""
Altura=100
Salto=3/5
NRebote=1

while NRebote<11:
    print("Rebote numero:", NRebote, "cuya altura es:", round(Altura*Salto,4), "mts.")
    NRebote=NRebote+1
    Altura=Altura*Salto
    
