# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:30:35 2017

@author: Admin
"""

def deep_reverse(lst):
    lst.reverse()
    for lstlst in lst:
        lstlst.reverse()