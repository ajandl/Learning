# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:21:22 2017

@author: Admin
"""

x = 25.0
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
    print(guess)

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))