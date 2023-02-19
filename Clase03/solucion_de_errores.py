# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
# Ejercicio 3.1: Semántica

#def tiene_a(expresion):
#    n = len(expresion)
#    i = 0
#    while i<n:
#        if expresion[i] == 'a':
#            print(f'Detecto {expresion[i]}')
#            return True
#        else:
#            print('No')
#            return False
#        i += 1

#tiene_a('UNSAM 2020')
#tiene_a('abracadabra')
#tiene_a('La novela 1984 de George Orwell')

# Para este ejercicio, probé dos cosas a partir de los problemas vistos:
#   1) Se detecta solo el primer caracter de la cadena (lo cual no sirve, esta mal)
#   2) Coloqué un print para cada caso del if, para chequear si se cumple el condicional
#   3) Se comento en return false para que no salga del while al leer el primer caracter de la 
#       expresion.


# Codigo corregido:
def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i<n:
       if expresion[i] == 'a':
           print(f'Detecto {expresion[i]}') # Para testear
           return True
       else:
           print('No') # Para testear
           #return False 
       i += 1


tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
# Ejercicio 3.2: Sintaxis
#def tiene_a(expresion)
#    n = len(expresion)
#    i = 0
#    while i<n
#        if expresion[i] = 'a'
#            return True
#        i += 1
#    return Falso

#tiene_a('UNSAM 2020')
#tiene_a('La novela 1984 de George Orwell')

# Detecte errores de sintaxis en:
#   1) Linea 'def tiene_a(expresion) donde faltaba ":"
#   2) Linea while i<n donde faltaba ":"
#   3) Linea if expresion[i] = 'a' donde faltaba ":" y un "="
#   4) Linea de return Falso --> Falso deberia ser False

# Corregido:
def tiene_a(expresion):
   n = len(expresion)
   i = 0
   while i<n:
       if expresion[i] == 'a':
           return True
       i += 1
   return False


tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3: Tipos
# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#             print(tiene)
#         i += 1
#     return tiene

# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)

# Se ve que tiene_uno(1984) está mal ya que se meto en la función un dato tipo int en lugar 
#de un string. Se solucionó colocando comillas.

# Corregido:
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
            print(tiene)
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')



#%%
# Ejercicio 3.4: Alcances
# def suma(a,b):
#     c = a + b
    
# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

# Al correr el programa da que 2 + 3 = None
# Hay que colocar un return al final de la funcion

# Corregido:
def suma(a,b):
    c = a + b
    return c #CORRECION ACA.

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")



#%%
# Ejercicio 3.5: Pisando memoria

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

# El problema es que se pisan los valores de una fila con la anterior. Esto se debe a que
#se le da un valor a cada registro[encabezado[n]], que en este caso son los valores de la 
#ultima fila del archivo.

# Corregido:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f) #Con esto leo el archivo que abri antes
        encabezado = next(filas) #solo leo el encabezado de las primeras filas que son 
                                #"nombre" "cajones" "precio" y me salteo esto en el for
        for fila in filas:
            registro = dict(zip(encabezado, (fila[0], int(fila[1]), float(fila[2]))))
            #con zip haciamos algo del tipo (a,b,c)(nom,cajo,pre)=(a,nom)(b,cajo)(c,pre)
            # y con dict armo el diccionario de tamaño 3 con esas 3 claves{'x':'x', 'y':caj, 'z':pre}
            #caj y pre son int por eso no tienen ''
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
