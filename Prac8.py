#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:10:57 2024

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([2.0,4.0,6.0,8.0,10.0])
y=np.array([42.0,48.4,51.3,56.3,58.3])
N=len(x)
den=N*np.inner(x,x)-(sum(x))**2.0

A=(np.inner(x,x)*sum(y)-sum(x)*np.inner(x,y))/den
B=(N*np.inner(x,y)-(sum(x)*sum(y)))/den
plt.scatter(x,y)


X=np.linspace(0.0,12.0)
Y=B*X+A
plt.plot(X,Y,"--",label="Fitted line")
plt.legend()
plt.show()