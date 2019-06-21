#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:51:38 2019

Geometric progression for clustering

@author: praphul
"""
import numpy as np

Sn = 1.0 # Length of the domain

r = 1.02 # Gp ratio 

n = 200 # No. of elements

a0 = Sn * (r-1)/(r**n-1) # First term which corresponds to first delx

a = []

#a.append(a0)

for i in range(1,n+1):
    a.append(a0*(r**(i-1)))

print('First distance height is',a0)

# Verify that the sum of the terms equals distance 

sum_1 = np.sum(a)

print('Sum of n terms (Total distance) is',sum_1)