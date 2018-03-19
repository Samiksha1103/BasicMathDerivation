# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:11:01 2018

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import math 
from sympy import var
from sympy import sympify

#arr_x=np.array([1,2,3,4])
#arr_y=np.array([3,5,2,8])
user_fun=str(input())

def fun(a):
    x= var('x')
    
    evalu= sympify(user_fun)
    epr=evalu.subs(x,a)
    #y= math.sin(a)
    return epr
    
a = 0
b = 2*math.pi
#b=input()
spacing = .01
no_of_spacing = ((b-a)/spacing)
v =  np.linspace(a,b,no_of_spacing)
'''p=np.array([])
for i in range(0,len(v)):
    q=fun(v[i])
    p=np.append(p,q)
plt.plot(v,p)'''
#print(v) 
#plt.plot(arr_x,arr_y)
arr=np.array([])
for i in range(0,len(v)):
    c = fun(v[i]+spacing)
    d=fun(v[i])
    e=((c-d)/spacing)
    
    arr = np.append(arr,e)
#print(arr)
   
plt.plot(v,arr)
    
    
    
    