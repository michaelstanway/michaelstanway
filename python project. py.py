# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:22:32 2020

@author: micha
"""
#Exercise 1
#Part a
from numpy import *
from matplotlib.pylab import *

def f(x):
    return (cos(x))**2

#Set the number of points and interval used
n = 100
a = -2
b = 2

#Array with n+1 points on [a, b]
x = linspace(a ,b ,n+1)
y = f(x)

#First make an array of zeros in which to store the derivative
dydx = zeros(n+1)

#Find the step−size
h = (b-a)/(n)

#Calculate the derivative, correct to first order
for i in range(n):
    dydx[i] = (y[i+1]-y[i])/h
#Need alternative form at end point
dydx[n]=(y[n]-y[n-1])/h

#Create an array of zeros in which to store the errors
error = zeros(n+1)

#Calculate the errors and organise them withing the array
#Square and then root the errors given so that you get their magnitude, this will counteract any sign changes that would affect what the maximum error is shown to be
for i in range(n):
    error[i] = sqrt((-sin(2*x[i])-dydx[i])**2)
error[n] = sqrt((-sin(2*x[n])-dydx[n])**2)

#print the largest error value
print("The maximum error is", max(error))

#print the corresponding value of x
for i in range(n+1):
    if error[i] == max(error):
        print("The value of x for which the max error occurs is", x[i])

#Part b
#Create an array for h containing 0.1, 0.01,...,1x10^-12        
p = 12

h = zeros(p)

for i in range(p):
    h[i] = 1/10**(i+1)

for i in range(p):
    dydx_0 = (f(1.56+h[i])-f(1.56))/h[i]
    error = -sin(2*1.56)-dydx_0
    print("The error, when h =", h[i], ", is ", error)

print("The results tend to a greater and greater degree of accuracy (with the error decreasing by a roughly factor of 10 each time), until h = 1e-10 when the error begins to get larger again. I am unsure why this is as it should consistently get more accurate so my guess is that it is to do with the way that the computer is computing the numbers as opposed to the underlying maths")



#Exercise 2
#Part a
from numpy import *
from matplotlib.pylab import *

def f(x):
    return x*arctan(x)

#Set the number of points and interval used
n = 100
a = 0
b = 2

#Array with n+1 points on [a, b]
x = linspace(a ,b ,n+1)
y = f(x)

#First make an array of zero sin which to store the derivative
dydx = zeros(n+1)

#Find the step−size
h = (b-a)/(n)
print(h)
#Calculate the derivative, correct to first order
for i in range(n):
    dydx[i] = (y[i+1]-y[i-1])/(2*h)
#Need alternative form at end point and start point
dydx[0] = (y[2]-y[0])/(2*h)
dydx[n] = (y[n]-y[n-2])/(2*h)

#Plotting the graph
plot(x, y)
plot(x, dydx)
xlabel("x")
ylabel("y")
title("The plot of f(x) and its derivative on the interval [0, 2]")
legend(["xarctan(x)", "dydx"])


#part b
#to find dydx at 1 
d = 0.016
dydx_1 = (f(1+d)-f(1-d))/(2*d)
#varying d shows that the value to 4 dp is 1.2854
print("To 4dp the value of df/dx at 1 is 1.2854")
print("To reach this degree of accuracy with a first order scheme you would need to set d to something of the order 10^-2 smaller than for the second order scheme")
#varying d you find that at 0.016 it reaches sufficient accurracy



#Exercise 3
from numpy import *

print("fx = (f(xi+1, yi)-f(xi-1,yi))/(2*h)")
print("fy = (f(xi, yi+1)-f(xi,yi-1))/(2*h)")
#Where fx and fy stand for the partial derivatives of f in terms of x and y respectively taken at the point (xi, yi)

def f(x, y):
    u = x*y*exp(-x**2-2*y**4)
    return u

h = 0.0001

fx = (f(1+h, 1)-f(1-h, 1))/(2*h)
fy = (f(1, 1+h)-f(1, 1-h))/(2*h)

print(fx)
print(fy)


#For h = 0.1
x1 = -0.048961092769509613
y1 = -0.33745917926041075

#For h = 0.05
x2 = -0.04957986068553834
y2 = -0.3457031726175443

#For h = 0.025
x3 = -0.0497352217465169
y3 = -0.34780510149784905

print((x1-x2)/(x2-x3))
3.982773496340285 #Very close to 4
print((y1-y2)/(y2-y3))
3.9221086090878075 #Very close to 4

#Therefore the scheme is indeed second order accurate

print("To 4dp fx = 0.0498 and fy = 0.3485")

fx = -0.0498
fy = -0.3485

#Unit vector for v = 1/sqrt(13)(2i-3j)
dd = (2*fx-3*fy)/sqrt(13)
print("The directional derivative of f(x, y) at point (1, 1) in the direction given by the vector, v = 2i-3j, is", dd)
