# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:34:23 2020

@author: micha
"""
#Question 1
#Part a
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

#Part b
#By working out the absolute values for the error at n=16 and n=32 it is clear that the absolute error is proportional to n^2. Since h is proportional to n^(-1), this means that the absolute error is proportional to h^2.
#Create values that caculate the integral with n at 16 and 32
w = trap_rule(f, -1, 1, 16)
q = trap_rule(f, -1, 1, 32)

#Calculate the average of the proportion between the absolute values when n is doubled (h is halved). I have taken the rounding of this as the variation between the actual value and the integer value is negligible (this difference is caused by the fact that it is based off of approximations). As the proportion calculated will equal 2^p (since n was doubled), the log of this value (with a base of 2) need to be taken to find the actual value for p. 
p = log2(round(((v-u)/(v-w)+(v-w)/(v-q))/2))

#Print a statement giving the value of p
print("By varying h it is clear that p =", p)

#Part c
from numpy import *
from matplotlib.pylab import *

#Define the function given
def f(x):
    return e**(-(sin(x)**2))

#Define the function used to find the approximation
def trap_rule(f, a, b, n):
    #Find the width of intervals
    h = (b-a)/n
    #Start by taking the terms outside the summation in eqn(1)
    integral = h/2*(f(a)+f(b))

    #Now we need the sum terms
    for i in range(1, n):
        integral = integral+h*f(a+i*h)

    return integral

#Create the value for J
J = trap_rule(f, 0, 2, 1000)

#The function below was used to help me find the value of z to four dp. Using a value for n of 1000 was more than enough to ensure the desired degree of accuracy. I varied the value of n to see whether with more and more accuracy the value of the fourth or fifth decimal point would change (as to values of n of this magnitude, the time taken to make the calculation is negligible and can be varied to much greater accuracies with ease) in any meaningful way. Once it was clear that this was not happening, no matter the increase in degrees of accuracy, I accepted 1.1810 as the value for J.
#print(J)

print("The value of J to four decimal places is 1.1810")

#Part d
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

#Label the axis and title the graph
xlabel("x")
ylabel("K(x)")
title("Exercise 1d")

#Question 2
from numpy import *
from matplotlib.pylab import *

#Define a function that will be suitable to calculate exactly and to approximate in order to compare
def f(x, y):
    return sin(x)*cos(y)

#Define a function to calculate the double trap rule
def double_trap_rule(f, a, b, c, d, nx, ny):
    #Find the width of the intervals
    hx = (b-a)/nx
    hy = (d-c)/ny
    
    #Finding the first set of additions
    u = (hx*hy/4)*(f(a, c) + f(a, d) + f(b, c) + f(b, d))
    
    #Finding the second set of additions
    #Create two arrays of zeroes of size ny and nx respectively, this allows for each value of x and y needed to be stored and used to work out the values within the sums given in equation 2 of the project instructions.
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
    
    #Create a value w to store the next set of sums
    w = 0  
    
    for j in range(nx):
        for i in range(ny):
            w = w + (hx*hy)*(f(x[j], y[i]))
    
    #Add all calculated values for the total value of the integration approximation
    integral = u + v + w
    
    return integral

g = 0.25
h = double_trap_rule(f, 0, pi/3, 0, pi/6, 1000, 1000)

print("I have chosen to test the accuracy of the double trap rule using the analytical result sin(x)*cos(y) (this is because it can be quite easily calculated exactly and so the error can be worked out to see how accurate the double trap rule is). I have bounded these such that the integral can be worked out to equal to 0.25.")
print("The exact value of the function given with a = 0, b = pi/3, c = 0, d = pi/6, is", g)
print("The value of the approximation obtained using the double trapezium rule is", h)
print("The absolute error is", g-h)
#When I attempt to vary nx and ny by a factor of two I found that when both are doubled, the value of the absolute error decreased by a factor of 0.5. Upon further inspection I found that doubling nx had almost no effect on the value for the absolute error while doubling ny showed that the absolute error is proportional to hy.
print("By varying hy and hx it is clear that the absolute error is proportional to hy^p, where p =", 1)
#Compare it to the single trap rule in terms of accuracy
print("The accuracy of this test can be compared to the single trap rule as i have set hx and hy to 1000 as well. When compared to the single trap rule it can be seen to be a factor of h more accurate (in this case 1000 times greater)")






