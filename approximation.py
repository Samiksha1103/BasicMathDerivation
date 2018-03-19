import matplotlib.pyplot as plt
import numpy as np
import math 
from sympy import var
from sympy import sympify

user_fun=str(input())

def fun(a):
    x= var('x')
    evalu= sympify(user_fun)
    epr=evalu.subs(x,a)
    return epr
    
a = 0
b = 2*math.pi

spacing = .01
no_of_spacing = ((b-a)/spacing)
v =  np.linspace(a,b,no_of_spacing)


x0=0
#dx=0.01
for i in range(0,len(v)):
    #if x0==2 and abs(v[i])<1:
    c =fun(x0)
    d=fun(x0+spacing)-fun(x0)
    e=d/spacing
    g=c+e*(v[i]-x0)
    
    #arr = np.append(arr,g)
#print(arr)
   
#plt.plot(v,arr)
print(g)   
    
    
    