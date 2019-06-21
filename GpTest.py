#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:05:44 2019

@author: praphul
"""

a0 = 1 

n = 8 

r = 3 

a = []

for i in range(1,n+1):
    a.append(a0*r**(i-1))    
    
print(a)