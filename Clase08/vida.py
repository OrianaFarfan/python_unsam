# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 11:41:31 2021

@author: pc
"""




#Importamos biblioteca
from datetime import datetime, date


# Funcion vida_en_seg
def vida_en_seg(nacimiento):
    '''le pasás tu fecha de nacimiento y devuelve la cantidad de segundos que viviste
    (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento)
    '''
    fecha_hoy = date.today()
    fecha_nacimiento = date(year = nacimiento[0], month = nacimiento[1], day = nacimiento[2])
    segundos_vida = fecha_hoy - fecha_nacimiento
    print("Segundos de vida: ", segundos_vida.total_seconds())


# Ingreso de la fecha
def nacimiento():
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))

    return (anio, mes, dia)


# Funcion Main
def main():
    fecha_nacimiento = nacimiento()
    vida_en_seg(fecha_nacimiento)


#_____________sys____________
if __name__ == "__main__":
    main()