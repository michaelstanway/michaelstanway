# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:03:13 2021

@author: micha
"""

# MT2507 Computing Project 
# Part 2: Helper functions

# 2a

import matplotlib.pyplot as plt
import numpy as np

# We have the following coupled system:
# dx/dt = x*(1-x-0.1exp(0.1y))
# dy/dt = y*(1-y-0.2exp(0.3x))

# Define this as a vector valued function:
def f(x,y):
    return np.array([x*(1-x-0.1*np.exp(0.1*y)), y*(1-y-0.2*np.exp(0.3*x))])

# Define the functions to generate the x_n+1 and y_n+1 values. These have been derived on paper analytically

def g(x, y):
    return -2*(x**2)*y - 0.2*np.exp(0.3*x)*(x**2) + 0.01*np.exp(0.1*y)*x*(y**2) + 2*x*y - 0.21*np.exp(0.1*y)*x*y + 0.002*np.exp(0.3*x + 0.1*y)*x*y + x + 0.2*np.exp(0.3*x)*x - 0.02*np.exp(0.3*x + 0.1*y)*x

def h(x, y):
    return -2*(y**2)*x - 0.1*np.exp(0.1*y)*(y**2) + 0.06*np.exp(0.3*x)*y*(x**2) + 2*x*y - 0.46*np.exp(0.3*x)*x*y + 0.006*np.exp(0.3*x + 0.1*y)*x*y + y + 0.1*np.exp(0.1*y)*y - 0.02*np.exp(0.3*x + 0.1*y)*y

def NRroot(x, y, g, h):
    for i in range(100):
        x = g(x, y)
        y = h(x, y)
    return [x, y]

# By inspection we know the three steady states are
W1 = [0,0]
W2 = [0,0.8]
W3 = [0.9,0]

# Choose an intial guess and find the root numerically
W4 = NRroot(0.85, 0.65, g, h)

print('The steady states are:')
print(W1,W2,W3,W4)

#To check, f(x, y) should be very close to [0,0]  
print(f(W4[0], W4[1]))


# Part 2b

import matplotlib.pyplot as plt
import numpy as np
import random


# We have the following coupled system:
# dx/dt = x*(1-x-0.1exp(0.1y))
# dy/dt = y*(1-y-0.2exp(0.3x))

# Define this as a vector valued function:
def f(x,y,t):
    return np.array([x*(1-x-0.1*np.exp(0.1*y)), y*(1-y-0.2*np.exp(0.3*x))])

# Now write a fourth order Runge-Kutta scheme to 
# integrate our function for a single time step:
def RK4step(x, y, t, h, f):
    k1 = h*f(x, y, t)
    k2 = h*f(x+k1[0]/2.0, y+k1[1]/2.0, t+h/2.0)
    k3 = h*f(x+k2[0]/2.0, y+k2[1]/2.0, t+h/2.0)
    k4 = h*f(x+k3[0], y+k3[1], t+h)
    return [x + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6, y + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6]

#Define the time step and number of steps to use
h=0.1
nsteps=1000

# Take a certain initial condition
for i in range(100):
    #Generate random numbers between 0 and 2 as your starting values for x and y
    x = random.randint(0,200)/100
    y = 2
    t = 0.0

    # Now solve the coupled ODEs for this initial condition
    # Do this by advancing the second order R-K scheme for several time steps
    
    # Arrays in which to store solutions
    xstore = []
    ystore = []
    xstore.append(x)
    ystore.append(y)



    # Use the second order Runge-Kutta method
    for n in range(nsteps+1):
        [x,y] = RK4step(x,y,t,h,f)
        t = t+h
        xstore.append(x)
        ystore.append(y)
        
    plt.plot(xstore, ystore)
    
for i in range(100):
    #Generate random numbers between 0 and 2 as your starting values for x and y
    x = random.randint(0,200)/100
    y = random.randint(0,10)/100
    t = 0.0

    # Now solve the coupled ODEs for this initial condition
    # Do this by advancing the second order R-K scheme for several time steps
    
    # Arrays in which to store solutions
    xstore = []
    ystore = []
    xstore.append(x)
    ystore.append(y)



    # Use the second order Runge-Kutta method
    for n in range(nsteps+1):
        [x,y] = RK4step(x,y,t,h,f)
        t = t+h
        xstore.append(x)
        ystore.append(y)
        
    plt.plot(xstore, ystore)
    
for i in range(100):
    #Generate random numbers between 0 and 2 as your starting values for x and y
    x = random.randint(0,10)/100
    y = random.randint(0,200)/100
    t = 0.0

    # Now solve the coupled ODEs for this initial condition
    # Do this by advancing the second order R-K scheme for several time steps
    
    # Arrays in which to store solutions
    xstore = []
    ystore = []
    xstore.append(x)
    ystore.append(y)



    # Use the second order Runge-Kutta method
    for n in range(nsteps+1):
        [x,y] = RK4step(x,y,t,h,f)
        t = t+h
        xstore.append(x)
        ystore.append(y)
        
    plt.plot(xstore, ystore)
    
for i in range(100):
    #Generate random numbers between 0 and 2 as your starting values for x and y
    x = 2
    y = random.randint(0,200)/100
    t = 0.0

    # Now solve the coupled ODEs for this initial condition
    # Do this by advancing the second order R-K scheme for several time steps
    
    # Arrays in which to store solutions
    xstore = []
    ystore = []
    xstore.append(x)
    ystore.append(y)



    # Use the second order Runge-Kutta method
    for n in range(nsteps+1):
        [x,y] = RK4step(x,y,t,h,f)
        t = t+h
        xstore.append(x)
        ystore.append(y)
        
    plt.plot(xstore, ystore)

X = np.array([W1[0], W2[0], W3[0], W4[0]])
Y = np.array([W1[1], W2[1], W3[1], W4[1]])

# Make a plot of this solution
plt.scatter(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solutions to the ODE')
plt.xlim(0,2)
plt.ylim(0,2)

# I have generated many intial conditions around the boundaries


