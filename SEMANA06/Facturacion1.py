# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:50:15 2022

@author: LUIS
"""

# Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconsubtotal(subtotal):.2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")