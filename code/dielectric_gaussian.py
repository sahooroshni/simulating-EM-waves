# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:07:10 2022

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



#initialising 
t = 0 

#iterating 
while t<tmax: 
    
    
    
    pulse= np.exp(-0.5*((40-t)/12)**2)      #gaussian source 
    ez[5] = pulse   #putting gaussian source in the middle of sample space 
    
    #update equations 
        
    for p in range(100,len(ez)-1):
        e_r = 4
        ez[p] = ez[p] - ((0.5/e_r)*(hy[p] - hy[p-1]))
    
    for p in range(1,100):
        e_r = 1
        ez[p] = ez[p] - ((0.5/e_r)*(hy[p] - hy[p-1]))
    
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
    
        
    if t==100 or t==200 or t==250 or t==325:
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