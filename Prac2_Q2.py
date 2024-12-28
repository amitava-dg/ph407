#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:15:33 2024

@author: student
"""

M=[]

m=int(input("Enter the number of rows of the matrix\n"))
n=int(input("Enter the number of columns of the matrix\n"))

print("Enter the elements of the matrix row wise")

for i in range(m):
    R=[]
    for j in range(n):
        R+=[eval(input())]
    M+=[R]

Tr=0.0
print("The input array is")
for i in range(m):
    Tr+=M[i][i]
    print(M[i])

#Additional: Find Trace of the Matrix    
print("Trace of the matrix is ", Tr)
    