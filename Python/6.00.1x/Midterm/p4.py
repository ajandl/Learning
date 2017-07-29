# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 23:03:03 2017

@author: Admin
"""

def closest_power(base, num):
    guess = 0
    while base**guess < num:
        guess += 1
#        print("Out:", base**guess)
        if (base**guess - num) >= (num - base**(guess-1)):
#            print(guess, ' ', base**guess)            
            guess -= 1
            break
        
#        print(guess)
    
    return guess