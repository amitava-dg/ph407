#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:12:53 2024

@author: student
"""

import numpy as np

n=3

X=np.zeros(3)
A=np.array(((1,2,3),(4,5,6),(7,8,10)),dtype=(float))
Y=np.array((10,20,31))

for i in range (n):
    for j in range (i+1,n):
        c=A[j][i]/A[i][i]
        A[j]=A[j]-c*A[i]
        Y[j]=Y[j]-c*Y[i]
        
for i in range (n-1,-1,-1):
    S=0
    for j in range(i+1,n):
        S=S+A[i][j]*X[j]
    X[i]=(Y[i]-S)/A[i][i]
    
print("MATRIX:\n",A)
print("ROOTS\n",X)
    
