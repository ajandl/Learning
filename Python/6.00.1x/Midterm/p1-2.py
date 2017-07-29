# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:04:40 2017

@author: Admin
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x