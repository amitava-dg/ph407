#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:25:17 2024

@author: student
"""

import numpy as np

A=np.matrix([[2,1,2],[4,2,4],[2,1,2]])
X=np.matrix([[1],[1],[1]])
tol=10.0
R=0.0

while(tol>=0.001):
    old=R
    Y=X
    X=A*X
    R=(np.transpose(Y)*X)/(np.transpose(Y)*Y)
    tol=abs(R-old)

print("Largest Eigenvalue:\n",R)
print("Normalized Eigenvector:\n",Y/np.sqrt(np.transpose(Y)*Y))