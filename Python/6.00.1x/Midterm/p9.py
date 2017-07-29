# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:27:20 2017

@author: Admin
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatList = []
    
    for i in range(len(aList)):

        if type(aList[i]) == list:
#            print("found another list", aList[i])
            flatList.extend(aList[i])
#            print("After flattening once:", flatList)
            return flatten(flatList) + flatten(aList[i+1:])
        else:
#            print("found base case, current list", aList[i])
            flatList.append(aList[i])
            
    return flatList
 