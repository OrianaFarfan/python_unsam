# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:28:34 2021

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


directorio = '../Data'
archivo1 = 'arbolado-en-espacios-verdes.csv'
fname1 = os.path.join(directorio,archivo1)
df_parques = pd.read_csv(fname1)
archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
fname2 = os.path.join(directorio,archivo2)
df_veredas = pd.read_csv(fname2, low_memory = False)

##Defino las columnas para cada csv
cols1 = ['altura_tot', 'diametro', 'nombre_cie']
cols2 = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']

##Selecciono las lineas y columnas correspondientes a las tipas
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols1].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols2].copy()

##Renombro las columnas para ambos archivos
df_tipas_parques = df_tipas_parques.rename(columns = {'altura_tot':'Altura',
                                                    'diametro':'Diametro',
                                                    'nombre_cie':'Nombre científico'})

df_tipas_veredas = df_tipas_veredas.rename(columns = {'altura_arbol':'Altura',
                                                    'diametro_altura_pecho':'Diametro',
                                                    'nombre_cientifico':'Nombre científico'})


##Agrego la columna ambiente
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'


##Junta ambos datasets con el comando
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


##Boxplots
df_tipas.boxplot('Diametro', by = 'Nombre científico')
df_tipas.boxplot('Altura', by = 'Nombre científico')
plt.show()