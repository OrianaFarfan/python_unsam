#Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar 
#del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

#%%
def tabla(n):
    n = n+1 #le sumamnos 1 porque necesitamos empezar de 0 y llegar a 9
    print('.      .', end = '')

    for i in range(n):
        print(f'{i:^5}', end = '')
     
#x = range(6)
#for n in x:
#    print(n) #imprime 0 1 2 3 4 5 

    
    print('\n.      .--------------------------------------------------', end = '') #hacemos un salto de linea con \n

    for x in range (n):
        mult = 0 #inicializamos multip
        print() #es como un salto de linea 
        print(f'{x:>5}|', end = '')

        for y in range(n): #ciclo se repite 9 veces
            print(f'{mult: >5}', end = '')
            mult += x #es como que x viene desde el primer for, toma valores de 0 a 9 por eso en la primera fila 
            #son puros 0
            #despues se inicia mult en 0 pero va sumando de 1 en 1, ya que ahi x toma valor 1.
            #despues se inicia mult en 0 pero se va sumando 2 en 2 ya que x toma el valor 2 --> 9+1 ciclos

tabla(9)
#%%