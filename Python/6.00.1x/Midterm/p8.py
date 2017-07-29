# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:17:24 2017

@author: Admin
"""

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    
    Assume functions f and g are defined for you. 

    f takes in an integer, applies a function, returns another integer 
   
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    Lcopy = L.copy()    
    
    for elem in Lcopy:
        if not g(f(elem)):
            L.remove(elem)
            
    if len(L) > 0:
        return max(L)
    else:
        return -1