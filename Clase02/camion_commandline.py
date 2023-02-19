# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:50:59 2021

@author: pc
"""

# Abre archivo camion.csv ('Data/camion.csv')
#lee las lineas y calcula el precio pagado por los
#cajones cargados en el camion


#Bibliotecas
import sys
import csv


# Funcion costo_camion
def costo_camion(file_name):
    # Variables
    costo = 0
    
    # Abro archivo camion.csv
    #file = open(file_name, 'rt') era antes sin el import csv 
    file = open(file_name)
    rows = csv.reader(file)
    
   
    head = next(rows) # Guardo cabecera en head
    print('{0:15s} {1:15s} {2:15s}'.format(head[0], head[1], head[2]))  # Imprimo cabecera para formar una "tabla"
    
   
    for line in file:  # Imprimo datos linea x linea y calculo precio de cajones
        row = line.split(',')
        print('{0:15s} {1:15s} {2:15s}'.format(row[0], row[1], row[2]))
        try: # Si no hay datos faltantes, hace la cuenta
            costo = costo + (float(row[1]) * float(row[2]))
        except ValueError: # Si faltan datos, tirame un warning
            print('Error detectado en fila', row[0])
    
    file.close() # Cierro archivo camion.csv
    
   
    return (costo)

# Dado en el informe
if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'missing.csv'

# Resultado
costo = costo_camion(file_name)
print('\nTotal pagado por los cajones es:', round(costo,2))


