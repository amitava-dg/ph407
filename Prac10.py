#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:15:20 2024

@author: student
"""

import numpy as np

x=np.linspace(0.0,1.0,10)

def f(x):
    return(x**0.5)

#Trapezoidal
A=0.0
for i in range (len(x)-1):
    A=A+0.5*(f(x[i+1])+f(x[i]))*(x[i+1]-x[i])
    
print(A)

#Simpson's One-Third
x=np.linspace(0.0,1.0,11)
A=f(x[0])+f(x[len(x)-1])
for i in range (1,len(x)-1):
    if(i%2!=0):
        A+=4.0*f(x[i])
    else:
        A+=2.0*f(x[i])
A=(x[1]-x[0])*A/3.0
print(A)

#Simpson's Three-Eight
x=np.linspace(0.0,1.0,13)
A=f(x[0])+f(x[len(x)-1])
for i in range (1,len(x)-1):
    if(i%3!=0):
        A+=3.0*f(x[i])
    else:
        A+=2.0*f(x[i])
A=3.0*(x[1]-x[0])*A/8.0
print(A)