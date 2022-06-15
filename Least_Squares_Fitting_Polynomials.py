# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:12:19 2022

@author: Karan

Least Squares Fitting Polynomial
- by Manuel A. Diaz @ Univ-Poiters / ENSMA, 2021
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

plt.close('all')

class LA:
    def __init__(self, case_select):
        self.case_select = case_select
    
    def polyfit_case_gen(self):
        
        if (self.case_select == 1):
            self.n = 100
            self.x = np.linspace(-1,1,self.n).T
            self.y = 1.0/(1 + 25 * self.x**2) + 1e-1 * \
                np.random.randn(self.n,1)
            
            #### Fit polynomial of order k ####
            self.k = 6

        elif (self.case_select == 2):
            self.x = np.arange(0,25,1)
            self.n = len(self.x)
            self.y = np.array([110.49,  73.72,  23.39,  17.11,  20.31,  29.37,  74.74, \
                117.02, 298.04, 348.13, 294.75, 253.78, 250.48, 239.48, \
                236.52, 245.04, 286.74, 304.78, 288.76, 247.11, 216.73, \
                185.78, 171.19, 171.73, 164.05])
            
            #### Fit polynomial of order k ####
            self.k = 8

        plt.figure(num='Noisyt Data visualization')
        plt.plot(self.x, self.y)
        plt.grid(b=True)
        
        return self.x, self.y
       
    def Vandermonde(self, x, k):
        n = len(x)
        m = k
        A = np.repeat(x[:,None],m,axis=1)
        
        for i in range(n):
            A[i,:] = np.power(A[i,:], np.arange(0,k,1))
        
        return A
    
    
        

case_select = 1

polyfit_gen = LA(case_select)

if (case_select == 1):
    n = 100
    x = np.linspace(-1,1,n).T
    y = 1.0/(1 + 25 * x**2) + 1e-1
    y = y[:,None] * np.random.randn(n,1)
    
    #### Fit polynomial of order k ####
    k = 6

elif (case_select == 2):
    x = np.arange(0,25,1)
    n = len(x)
    y = np.array([110.49,  73.72,  23.39,  17.11,  20.31,  29.37,  74.74, \
                  117.02, 298.04, 348.13, 294.75, 253.78, 250.48, 239.48, \
                      236.52, 245.04, 286.74, 304.78, 288.76, 247.11, 216.73, \
                          185.78, 171.19, 171.73, 164.05])
    
    #### Fit polynomial of order k ####
    k = 8

plt.figure(num='Noisyt Data visualization')
plt.plot(x, y, 'ok')
plt.grid(b=True)

#### Polynomial fitting of kth order ####

#### 1. Least Square fitting ####
x_poly = np.linspace(np.min(x), np.max(x), n)#2
P1 = np.polyfit(x, y, k)
plt.plot(x_poly, np.polyval(P1, x_poly), '-')

#### 2. Using LA operations ####
X = polyfit_gen.Vandermonde(x, k+1)
P2 = np.linalg.lstsq((X.T @ X),(X.T @ y),rcond=None)[0] 
plt.plot(x_poly, np.polyval(np.flipud(P2), x_poly), '-.')

