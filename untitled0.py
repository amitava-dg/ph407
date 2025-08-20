# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 18:39:15 2025

@author: Amitava
"""

import torch
import numpy as np
import deepxde as dde
import matplotlib.pyplot as plt

theta_V=0.590 #radians
delta_m2=8.0e-5 #eV2
E=1.0e9 #eV
omega=1.52e15*0.5*delta_m2/E
V=2.5e-13/omega

Omega=np.array([np.sin(2*theta_V),0,np.cos(2*theta_V)-V])

def ode_system (tau,P):
    Px=P[:,0:1]
    Py=P[:,1:2]
    Pz=P[:,2:3]
    
    Px_dtau=dde.grad.jacobian(P, tau, i=0,j=0)
    Py_dtau=dde.grad.jacobian(P, tau, i=1,j=0)
    Pz_dtau=dde.grad.jacobian(P, tau, i=2,j=0)
    
    return [
        Px_dtau-(Omega[1]*Pz-Omega[2]*Py),
        Py_dtau-(Omega[2]*Px-Omega[0]*Pz),
        Pz_dtau-(Omega[0]*Py-Omega[1]*Px),
    ]


geom=dde.geometry.TimeDomain(0.0,2.0*np.pi)

data = dde.data.PDE(geom, ode_system, [], 3000, num_test = 3000)


def output_transform(tau, P):
    Px = P[:, 0:1]
    Py = P[:, 1:2]
    Pz = P[:, 2:3]
    return torch.cat(
        [Px * tau,
         Py * tau,
         Pz * tau + 1.0,
         ],
        axis=1,
    )


layer_size = [1] + [64] * 6 + [3]
activation = "tanh"
initializer = "Glorot normal"
net = dde.nn.FNN(layer_size, activation, initializer)

net.apply_output_transform(output_transform)
model = dde.Model(data, net)
model.compile("adam", lr=0.001)
losshistory, train_state = model.train(iterations=1000)

model.compile("L-BFGS")
losshistory, train_state = model.train()
dde.saveplot(losshistory, train_state, issave=True, isplot=True)

t = np.linspace(0, 2*np.pi, 100)[:, None]
y_pred=model.predict(t)
