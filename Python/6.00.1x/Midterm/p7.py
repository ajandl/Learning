# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:56:34 2017

@author: Admin
"""

def f(val1, val2):
    return val1 + val2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    
    d1c = d1.copy()
    d2c = d2.copy()
    
    intersect = {}
    difference = {}
    
    while len(d1c) > 0:
        (d1key, d1val) = d1c.popitem()
        
        if d1key in d2c:
            intersect[d1key] = f(d1val,d2c[d1key])
            del d2c[d1key]
        else:
            difference[d1key] = d1val
        
    difference.update(d2c)
    
    return(intersect, difference)