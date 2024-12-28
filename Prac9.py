#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:33:34 2024

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#GAUSSIAN CURVE FITTING WITH GENERATED DATA
N=100

def Gaussian (x,x0,sigma):
    return(np.exp(-0.5*(x-x0)**2.0/sigma**2.0))

#def Gaussian_der(x,x0,sigma):
#    return(-0.5*2*(x-x0)*np.exp(-0.5*(x-x0)**2.0/sigma**2.0)/sigma**2.0)

x=np.linspace(-10.,10.,N,endpoint=True)+0.01*np.random.random(N)
y=Gaussian(x,1.0,2.0)+0.01*np.random.random(N)

params,error=curve_fit(Gaussian, x, y)

der=np.zeros(N)
der_fit=np.zeros(N)

y_fitted=Gaussian(x,*params)
plt.figure(figsize=(20,10))
plt.plot(x,y_fitted,c="red")
plt.scatter(x,y,c="black")

print(params)

#NUMERICAL DERIVATIVE OF THE GAUSSIAN
for i in range(1,N-1):
    der[i]=(y[i+1]-y[i-1])/(x[i+1]-x[i-1])
    der_fit[i]=(y_fitted[i+1]-y_fitted[i-1])/(x[i+1]-x[i-1])
    
plt.scatter(x,der)
#plt.scatter(x,der_fit)

#FWHM
maxima=max(y_fitted)
half_max=maxima/(2.0**0.5)
plt.axhline(half_max,linestyle="--")
plt.show()

for i in range(N-1):
    if((y_fitted[i+1])>half_max)and(y_fitted[i]<half_max):
        left=x[i]
        print(left)
    if((y_fitted[i+1])<half_max)and(y_fitted[i]>half_max):
        right=x[i]
        print(right)
        
print("FWHM:\t",(right-left))


