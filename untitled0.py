# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 22:55:19 2025

@author: Amitava
"""

import numpy as np
import deepxde as dde
import matplotlib.pyplot as plt
import torch

"""
theta_V=0.583 #rads
delta_m2=7.5e-5 #eV2
E=10.0e6 #eV
omega = 0.5*delta_m2/E*1.52e15 #rad s-1
"""
theta_V=0.583 #rads
delta_m2=7.5e-5 #eV2 c-4
E=10.0e6 #eV
omega = 0.5*delta_m2/E*1.25e15 #rad s-1

Omega=omega*np.array([-np.cos(2*theta_V),0,np.sin(2*theta_V)])


def ode_system (t,P):
    Px=P[:,0:1]
    Py=P[:,1:2]
    Pz=P[:,2:3]
    
    Px_dt=dde.grad.jacobian(P, t, i=0,j=0)
    Py_dt=dde.grad.jacobian(P, t, i=1,j=0)
    Pz_dt=dde.grad.jacobian(P, t, i=2,j=0)
    
    return [
        Px_dt-(Omega[1]*Pz-Omega[2]*Py),
        Py_dt-(Omega[2]*Px-Omega[0]*Pz),
        Pz_dt-(Omega[0]*Py-Omega[1]*Px)
    ]


geom=dde.geometry.TimeDomain(0.0,2.0*np.pi/omega)


ic_Px = dde.icbc.IC(geom, lambda t: 0.0, lambda _, on_initial: on_initial,
                    component=0)
ic_Py = dde.icbc.IC(geom, lambda t: 1.0e-6, lambda _, on_initial: on_initial,
                    component=1)
ic_Pz = dde.icbc.IC(geom, lambda t: 1.0, lambda _, on_initial: on_initial,
                    component=2)


data = dde.data.PDE(geom, ode_system, [ic_Px,ic_Py,ic_Pz], 3000
                    , num_test = 3000)

"""
def input_transform(t):
    return torch.cat(
        [
            torch.sin(omega*t),
            torch.cos(omega*t),
            t
        ],
        axis=1,
    )
"""

def output_transform(t, P):
    Px = P[:, 0:1]
    Py = P[:, 1:2]
    Pz = P[:, 2:3]
    return torch.cat(
        [Px * torch.sin(t) + 0.0,
         Py * torch.sin(t) + 1.0e-6,
         Pz * torch.sin(t) + 1.0,
         ],
        axis=1,
    )

layer_size = [1] + [64] * 6 + [3]
activation = "tanh"
initializer = "Glorot normal"
net = dde.nn.FNN(layer_size, activation, initializer)

#net.apply_feature_transform(input_transform)
net.apply_output_transform(output_transform)
model = dde.Model(data, net)
model.compile("adam", lr=0.001)
losshistory, train_state = model.train(iterations=3000)

model.compile("L-BFGS")
losshistory, train_state = model.train()
dde.saveplot(losshistory, train_state, issave=True, isplot=True)

# %%
t = np.linspace(0, 20.0, 1000)[:, None]
y_pred = model.predict(t)
plt.plot(t, y_pred[:,2], label="a1(t)")
plt.xlabel("t")
plt.ylabel("Pz")
plt.legend()
plt.show()
# %%

    