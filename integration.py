import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import var
from sympy import sympify

user_input=str(input())

def integration(a):
    x=var('x')
    evalu=sympify(user_input)
    result_eq=evalu.subs(x,a)
    return result_eq

a=0
b=2*math.pi
dx=0.01
no_of_slots=((b-a)/dx)

v=np.linspace(a,b,no_of_slots)

arr=np.array([])
sum=0
for i in range(0,len(v)):
    c = integration(v[i])
    #d=fun(v[i])
    #e=((c-d)/spacing)
    #F1= integration(e)
    #F2= integration(a+dx)
    Final=c*dx
    sum +=Final
    arr=np.append(arr,sum)
    
plt.plot(v,arr)