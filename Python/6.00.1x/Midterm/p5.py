# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 23:24:15 2017

@author: Admin
"""

def dotProduct(listA, listB):
    dP = 0
    for i in range(len(listA)):
        dP += listA[i] * listB[i]
    
    return dP