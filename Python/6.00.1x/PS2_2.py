# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:55:17 2017

@author: Admin
"""
balance = 999999
annualInterestRate = 0.18

""" Copy below here """

ub = balance
r = annualInterestRate

months = 12

hi = (ub*(1+r/12)**12)/12
lo = ub/12
paym = (hi + lo)/2

def remBal(months, ub, paym):
    
    if months == 0:
        return round(ub,2)
    else:
        ub -= paym
#        print("Balance: ", ub)
        if ub == 0:
            return round(ub, 2)
        ub += (r/12)*ub
        months -= 1
#        print ("Month ", months, ": Remaining balance = ", round(ub, 2))
        return remBal(months, ub, paym)


while abs(remBal(months, ub, paym)) > 0.01:
    if remBal(months, ub, paym) > 0:
        lo = paym
        paym = round((hi + lo)/2, 3)
    else:
        hi = paym
        paym = round((hi+ lo)/2, 3)
#        print("Payment: ", paym)

 
print("Lowest Payment: ", round(paym,2))
        