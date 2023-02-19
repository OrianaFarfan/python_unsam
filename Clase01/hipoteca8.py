# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:46:27 2021

@author: pc
"""

#Supongamos que David adelanta pagos extra de $1000/mes durante los primeros
#12 meses de la hipoteca.

#Modifica el programa para incorporar estos pagos extra y que imprima
#el monto total pagado junto con la cantidad de meses requeridos.

#hipoteca 1.8
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
while saldo > 0:
   
    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual-1000
        total_pagado = total_pagado + pago_mensual+1000
        mes = mes + 1
    else: 
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes = mes + 1

print("mes:", mes, "total pagado:", round(total_pagado,2)) 