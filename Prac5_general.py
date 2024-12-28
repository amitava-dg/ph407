#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:56:42 2024

@author: student
"""

import numpy as np

n=int(input("Enter the dimension of the coefficient matrix\t"))
A=np.zeros((n,n))
Y=np.zeros(n)
X=np.zeros(n)

print("Enter the elements corresponding to the equations")
for i in range(n):
    for j in range(n):
        A[i][j]=float(input())
        
print("Enter the elements of the RHS")
for i in range(n):
    Y[i]=float(input())

for i in range (n):
    for j in range (i+1,n):
        c=A[j][i]/A[i][i]
        A[j]=A[j]-c*A[i]
        Y[j]=Y[j]-c*Y[i]
        
for i in range (n-1,-1,-1):
    S=0.0
    for j in range(i+1,n):
        S=S+A[i][j]*X[j]
    X[i]=(Y[i]-S)/A[i][i]
    
print("UPPER TRIANGULAR MATRIX:\n",A)
print("RHS MATRIX AFTER OPERATIONS\n",Y)
print("ROOTS\n",X)