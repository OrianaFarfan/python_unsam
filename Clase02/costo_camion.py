# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 00:54:05 2021

@author: pc
"""

# costo_camion.py
# Abre archivo camion.csv ('Data/camion.csv')
#lee las lineas y calcula el precio pagado por los
#cajones cargados en el camion


# Importo biblioteca CSV
import csv


def costo_camion(file_name): # Defino funcion costo_camion
    
    costo = 0 # Variables
    
   
    #file = open('camion.csv', 'rt') --> seria antes
    file = open(file_name)  # Abro archivo camion.csv. 
    #NOTAR QUE AHORA SOLO USO OPEN, NO HAGO 'rt' COMO SEGUNDO PARAMETRO
    rows = csv.reader(file)
    
   
    header = next(rows)  # Salteo cabecera y la guardo
    
    # Imprimo datos y, a la vez, calculo precio de cajones
    for i, row in enumerate(rows, start=1):
        try: # Si no hay datos faltantes, hace la cuenta
            record = dict(zip(header,row))
            Ncajones = int(record['cajones'])
            Precio = float(record['precio'])
            costo += Ncajones * Precio
        except ValueError: # Si faltan datos, tirame un warning
            print(f'Fila {i}: No se puede interpretar: {row}')
   
    file.close() # Cierro archivo camion.csv
    
    
    return (costo) # Retorno con resultado

#%% Resultado
final = costo_camion('camion.csv') 
print('\nTotal pagado por los cajones es: $', round(final,2))


