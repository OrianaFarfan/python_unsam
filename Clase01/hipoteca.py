# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

#David solicitó un crédito a 30 años para comprar una vivienda, 
#con una tasa fija nominal anual del 5%. Pidió $500000 al banco y 
#acordó un pago mensual fijo de $2684,11.
#El siguiente es un programa que calcula el monto total que pagará David 
#a lo largo de los años:
    
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0: #Quiere decir que mientras que lo que se deba sea cero. O sea chau deuda. 
    saldo = saldo * (1+tasa/12) - pago_mensual  #Debe ser que lo dividio por 12 porque era una 
                                                #tasa anual y yo necesito una mensual.
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))