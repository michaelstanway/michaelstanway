# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:34:23 2020

@author: micha
"""
#Question 1
#Parts a&b
from numpy import *
from matplotlib.pylab import *

#Define the function to be approximated
def f(x):
    return 7/(3-2*x**2)

def trap_rule(f, a, b, n):
    #Find the width of intervals
    h = (b-a)/n
    #Start by taking the terms outside the summation in eqn(1)
    integral = h/2*(f(a)+f(b))

    #Now we need the sum terms
    for i in range(1, n):
        integral = integral+h*f(a+i*h)

    return integral

#v is the actual value of the integral
v = (7/sqrt(6))*(log((sqrt(3)+sqrt(2))/(sqrt(3)-sqrt(2))))
#u is the value of the approximation
u = trap_rule(f, -1, 1, 8)

print("The exact value of I is ", v)
print("The approximation obtained by using the trapezium rule with 8 intervals is ", u)

#The absolute error is the actual value - approx value
print("The absolute error is ", v-u)

#By working out the absolute values for n=16 and n=32 it is clear that the absolute error is proportional to n^2. Since h is proportional to n^(-1), this means that the absolute error is proportional to h^2.

#Create values that caculate the integral with n at 16 and 32
w = trap_rule(f, -1, 1, 16)
q = trap_rule(f, -1, 1, 32)

#Calculate the average of the proportion between the absolute values when n is doubled (h is halved). I have taken the rounding of this as the variation between this and the  
p = log2((((v-u)/(v-w)+(v-w)/(v-q))/2))


print("By varying h it is clear that p =", p)

#Parts c&d
from numpy import *
from matplotlib.pylab import *

def f(x):
    return e**(-(sin(x)**2))

def trap_rule(f, a, b, n):
    #Find the width of intervals
    h = (b-a)/n
    #Start by taking the terms outside the summation in eqn(1)
    integral = h/2*(f(a)+f(b))

    #Now we need the sum terms
    for i in range(1, n):
        integral = integral+h*f(a+i*h)

    return integral

J = trap_rule(f, 0, 2, 1000)

#The function below was used to find the value of z to four dp. Using a value for n of 1000 was more than enough to ensure the desired degree of accuracy.
#print(J)

print("The value of J to four decimal places is 1.1810")

c = 0
d = 5*pi
m = 1000

#Create an array of zeros the size of m
x = zeros(m+1)
K = zeros(m+1)

#Fill the array with the appropriate numbers (values of x between 0 and 5pi and their corresponding values for K)
for i in range(m+1):
    x[i] = i*((d-c)/m)
    K[i] = trap_rule(f, 0, x[i], 1000)

plot(x, K)
#Produces a wavey looking graph that looks like it oscillates arount a linear line with an equation of K = 5/8 x (with the gradient given there being a rough guess).

xlabel("x")
ylabel("K(x)")
title("Exercise 1d")

#Question 2
from numpy import *
from matplotlib.pylab import *

def f(x, y):
    return sin(x)*cos(y)


def double_trap_rule(f, a, b, c, d, nx, ny):
    #Find the width of the intervals
    hx = (b-a)/nx
    hy = (d-c)/ny
    
    #Finding the first set of additions
    u = (hx*hy/4)*(f(a, c) + f(a, d) + f(b, c) + f(b, d))
    
    #Finding the second set of additions
    #Create two arrays of zeroes of size ny and nx respectively
    y = zeros(ny)
    x = zeros(nx)
    #Create a variable v to contain the sum
    v = 0
    
    for i in range(ny-1):
        y[i] = c + (i+1)*hy
        v = v + (hx*hy/2)*(f(a, y[i])+f(b, y[i]))
        
    for j in range(nx-1):
        x[j] = a + (j+1)*hx
        v = v + (hx*hy/2)*(f(x[j], c)+f(x[j], d))
        
    w = 0  
    
    for j in range(nx):
        for i in range(ny):
            w = w + (hx*hy)*(f(x[j], y[i]))
            
    integral = u + v + w
    
    return integral
    
print(double_trap_rule(f, 0, pi/3, 0, pi/6, 2000, 2000))

#The error halves each time the values for nx and ny double so the value for p is -1
#The double integral of sinxcosy should be equal to 0.25 and so ive set the values as such and found that the approximation is roughly equal to it








