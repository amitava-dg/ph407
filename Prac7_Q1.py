#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:42:59 2024

@author: student
"""

def f(x):
    return(x**6.0-x-1)

def Secant():
    c=0
    tol=1.0
    print("Enter initial guesses:")
    x_old=float(input())
    x=float(input())
    
    if(f(x_old)*f(x)>0):
        print("Given initial guesses do not bracket a root. TRY AGAIN.")
        Secant()
    
    while(tol>10.0**-6.0):
        c+=1
        x_new = x -((f(x)*(x-x_old))/(f(x)-f(x_old)))
        tol=abs(x_new-x)
        x_old=x
        x=x_new
        
    print("ROOT\n",x_new)
    print("ITERATIONS\n",c)

Secant()