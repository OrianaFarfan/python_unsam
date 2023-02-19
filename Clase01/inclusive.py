# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:43:28 2021

@author: pc
"""

#Queremos hacer un traductor que cambie las palabras masculinas de una frase
#por su versión neutra. Como primera aproximación, completá el siguiente código
#para reemplazar todas las letras 'o' que figuren en el último o anteúltimo
#caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores'
#pasaría a ser 'todes somes programdores'. Guardá tu código en el archivo
#inclusive.py


frase = '¿cómo transmitir a los otros el infinito Aleph?'
palabras = frase.split()
print(palabras) # Para ver como queda la frase luego del split --> Se ve que me arma una lista con 
                                                                        #cada palabra
                        
i = 0 #Con este contador nos movemos en cada vector de la lista.
for palabra in palabras:
	if palabra[-1] == 'o': #Aca es si la ultima palabra de cada "vector" de la lista termina en o
		palabras[i] = palabra[:-1] + 'e' #Sera reemplazado por e
        
	elif (len(palabra) >= 2) and (palabra[-2] == 'o'): #Si la palabra tiene un largo mayor a 2 letras
                                                            #Y el anteultima palabra es o
                                                            
		palabras[i] = palabra[:-2] + 'e' + palabra[-1:]  #Es reemplazado en ese lugar por e 
                                        #Acordate que con [:,-2] no incluye a ese valor final
                                        #Por eso es reemplazado por ese +'e'
                                        
	i = i + 1 #Sumo para ir con el otro vector de la lista
    
    
frase_t = ' '.join(palabras)
print(frase_t)