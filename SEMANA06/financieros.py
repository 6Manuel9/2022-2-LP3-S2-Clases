# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:43:54 2022

@author: LUIS
"""

igv = 0.18

def obtenerIGVconsubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1 + 01.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)