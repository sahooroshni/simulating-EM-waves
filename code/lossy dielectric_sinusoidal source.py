# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:41:08 2022

@author: roshn
"""


import numpy as np 
import matplotlib.pyplot as plt 

#array for electric and magnetic fields 
ez = np.zeros(200)
hy = np.zeros(200)

#total iterations of time 
tmax = 1000


ez_1 = np.zeros(tmax)
ez_197 = np.zeros(tmax)

dx = 0.75/60
dt = dx/(2*3*10**8)
f = 400*(10**6)


#initialising 
t = 0 

#iterating 
while t<tmax: 
    
    
    
    pulse= np.sin(2*np.pi*f*dt*t)      #gaussian source 
    ez[5] = pulse   #putting gaussian source in the middle of sample space 
    
    #update equations 
        
    for p in range(100,len(ez)-1):
        sigma = 0
        e_r = 20
        e_0 = 8.5*(10**-12)
        eaf = (sigma*dt)/(2*e_r*e_0)
        ca = (1-eaf)/(1+eaf)
        cb = (0.5)/(e_r*(1+eaf))
        
        ez[p] = (ca*ez[p] ) - (cb*(hy[p] - hy[p-1]))
    
    for p in range(1,100):
        sigma = 0 
        e_r = 1
        e_0 = 8.5*(10**-12)
        eaf = (sigma*dt)/(2*e_r*e_0)
        ca = (1-eaf)/(1+eaf)
        cb = (0.5)/(e_r*(1+eaf))
        
        ez[p] = (ca*ez[p] ) - (cb*(hy[p] - hy[p-1]))
    
    #absorbing boundary conditions
    ez_1[t] = ez[1]
    ez_197[t] = ez[197]
    
    if t>2 or t==2: 
        ez[0] = ez_1[t-2]
        ez[198] = ez_197[t-2] 
        

    for m in range(len(hy)-2):
        hy[m] = hy[m] - (0.5*(ez[m+1] - ez[m]))
   
 
    
        
        
    t += 1          #iterating time
        
    #plotting 
    #plotting 
    def constant_function(x):
        return np.full(x.shape, 100)
    
        
    if t==500:
        p = np.linspace(0,199,200)
        
        fig, ax = plt.subplots(2)
        
        ax[0].plot(p,ez,label='T = {}'.format(t))
        ax[0].set_title('EM wave propagation in space')
        ax[0].plot(constant_function(p),p,'--',color='black',label='Dielectric Medium')
        ax[0].plot(-constant_function(p),p,'--',color='black')
        ax[0].set_ylabel('$E_{z}$')
        ax[0].set_xlabel('FDTD Cells')
        ax[0].set_xlim(0,199)
        ax[0].set_ylim(-1.5,1.5)
        ax[0].legend()
        
        ax[1].plot(p,hy,label='T = {}'.format(t))
        ax[1].plot(constant_function(p),p,'--',color='black',label='Dielectric Medium')
        ax[1].plot(-constant_function(p),p,'--',color='black')
        ax[1].set_ylabel('$H_{y}$')
        ax[1].set_xlabel('FDTD Cells')
        ax[1].set_ylim(-1.5,1.5)
        ax[1].set_xlim(0,199)
        ax[1].legend()