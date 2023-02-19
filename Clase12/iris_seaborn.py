# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:46:52 2021

@author: pc
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


iris_dataset = load_iris() #Asi cargamos los datos a la variable 

iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names) # Creo Dataframe de flores
iris_dataframe['target'] = iris_dataset['target'] #Cargo los datos de esa clave a otro diccionario


#Agrego los nombres a las claves [0,1,2] de iris_dataset['target']
#por ['setosa', 'versicolor', 'virginica'] de iris_dataset['target_names']
d_names = dict(zip([0,1,2], iris_dataset['target_names'])) #Donde a cada valor [0,1,2] asigno el nombre
names = [d_names[iris_dataset['target'][i]] for i in range (len(iris_dataset['target']))]

iris_dataframe['target_names'] = names # Creo la columna en el dataframe


#Variables para explorar
x_v=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
y_v=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

#Plot
p = sns.pairplot(data = iris_dataframe, x_v = x_v, y_v = y_v,
                 hue = 'target_names', diag_kind='hist', markers=["o", "s", "D"],
                 height = 2)
            
#Título de gráfico
p.fig.suptitle("Data Frame iris exploración de datos por tamaño\n"
             "sépalos vs. tétalos, largo y ancho")
plt.subplots_adjust(top= 0.9)

plt.show()