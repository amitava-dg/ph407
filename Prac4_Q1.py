#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:06:20 2024

@author: student
"""

x=[27,34,33,33,17,78,65]

for i in range (len(x)-1):
    for j in range (len(x)-i-1):
        if(x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]

print(x)