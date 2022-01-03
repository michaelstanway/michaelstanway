# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:44:33 2020

@author: micha
"""

from numpy import *
from matplotlib.pylab import *

def f(x):
    return sin(x)

n = 100
a = -5
b = 5

x = linspace(a ,b ,n+1)
y = f(x)
plot(x ,y )

plot(x ,y )
xlabel("x")
ylabel("y")
title("a first plot")
legend(["sin(x)"])

plot(x ,y ,"r")
plot(x ,cos(x) ,"b--")
xlabel("x")
ylabel("y")
title("Example with two plots at once")
legend(["sin(x)", "cos(x)"])


from numpy import *
from matplotlib.pylab import *

h = 0.000000001
x = 1
d = (exp(x+h)-exp(x))/h
print("For h = ", h, "the approximated derivative has value", d)

print("the error in approximation is", exp(1)-d)

def f(x):
    return sin(x)

#Set the number of points and interval used
n = 100
a = -5
b = 5

#Array with n+1 points on [a, b]
x = linspace(a ,b ,n+1)
y = f (x)

#First make an array of zero sin which to store the derivative
dydx = zeros(n+1)

#Find the step−size
h = (b-a)/(n)

#Calculate the derivative, correct to first order
for i in range(n):
    dydx[i]=(y[i+1]-y[i])/h
#Need alternative form at end point
dydx[n]=(y[n]-y[n-1])/h

