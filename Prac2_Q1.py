#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:03:19 2024

@author: student
"""

R=1.097E-2

for m in range(1,4):
    for k in range(1,5):
        wav=1.0/(R*((1/m)**2.0-(1/(m+k)**2.0)))
        print("Wavelength corresponding to m= "+str(m)+" and n= "+str(m+k), wav)