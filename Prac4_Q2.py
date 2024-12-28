#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:34:14 2024

@author: student
"""

import numpy as np

def f(x):
    return(x+np.exp(-1.0*x**2.0)*np.cos(x))

def Bis():
    low=float(input("Enter the lower guess "))
    high=float(input("Enter the higher guess "))
    mid=0.0
    
    eps=0.0001
    tol=1.0
    ite=0
    c=0
    
    while(tol>eps):
        if(f(low)*f(high)<0):
            ite+=1
            mid=0.5*(low+high)
            tol=abs(mid-low)
            if(f(mid)*f(low)<0):
                high=mid
            else:
                low=mid
            c=1
        else:
            print("GUESSES DO NOT BRACKET. RETRY.")
            Bis()
            return()
        
    if(c==1):   
        print("Number of iterations",ite)
        print("Root=",mid)
        
    return()

Bis()
