#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:28:51 2024
Gauss Jordan
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
    
    
for i in range(n):
    for j in range(n):
        if(i!=j):
            c=A[j,i]/A[i,i]
            A[j]=A[j]-c*A[i]
            Y[j]=Y[j]-c*Y[i]

for i in range(0,n):
    c=A[i,i]
    A[i]=A[i]/c
    Y[i]=Y[i]/c
    
print("THE DIAGONAL MATRIX:\n",A)
print("ROOTS\n",Y)
            
