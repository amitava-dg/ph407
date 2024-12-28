#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:53:47 2024

@author: student
"""

import math


def f(x):
    return(math.cos(x))
        
err=1.0
i=0
p_sum=0.0

x=float(input("Enter a value of x for cos(x)\t"))
print("\t")
print("cos(x)=",f(x))

while(err>0.002):
    p_sum = p_sum+((-1)**(i)*x**(2*i)/math.factorial(2*i))
    err=abs(1.0-(p_sum/f(x)))
    print("Number of terms",i+1)
    print("Partial sum:")
    print(p_sum)
    print("Relative % Error:")
    print(err*100,"%")
    print("\t\t")
    i=i+1
    
print("The sum reaches the required error (<0.2%) in ",i,"terms")