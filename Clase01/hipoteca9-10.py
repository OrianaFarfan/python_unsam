# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:08:49 2021

@author: pc
"""

saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
        pago_mensual = 2684.11
        mes=mes+1
        
        if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
                pago_mensual+=pago_extra
                
        if saldo<pago_mensual:
            pago_mensual=saldo*(1+tasa/12) 
            saldo = saldo * (1+tasa/12) - pago_mensual-pago_extra
            total_pagado = total_pagado + (pago_mensual+pago_extra)
          
       
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado=total_pagado+pago_mensual
        
        print(mes,round(total_pagado,2),round(saldo,2))
        
print("total pagado:",round(total_pagado,2))
print("mes:",mes)