# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:58:32 2022

@author: LUIS
"""

# Dado el total, calcular el IGV y el subtotal

import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")