# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:23:29 2017

@author: Admin
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x