#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:22:35 2024

@author: student
"""

def Pattern():
    rows=eval(input("Enter the number of rows\n"))
    
    if(rows!=int(rows)):
        print("Floating inputs with non zero decimals not allowed. Retry with integers >0.")
        Pattern()
    elif rows<1:
        print("Number of rows cannot be less than 1. Retry with integers >0.")
        Pattern()
    else:
        for i in range (1,int(rows)+1):
            print(i*"1")

Pattern()