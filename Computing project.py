# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:30:24 2021

@author: Michael Stanway
"""

# MT2507 Computing Project 

#Part 1: Single Species Population Model

# Part 1a
# Import the python packages required
import matplotlib.pyplot as plt
import numpy as np

# Define the function in the question
def F(x):
    return 0.001 - 0.4*x + (x**2/(1+x**2))
    
 
# Plot the function to find out how many roots there are and roughly where they lie

# Range of x values (chosen by hand)
x = np.arange(-0.5, 2.5,0.01)

# Make the plot
plt.plot(x, F(x))
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('F(x) on limited range')
plt.grid(True)
plt.show()

# From this we can see there are three roots, there is one different root in each of the regions (-0.25, 0.25), (0.25, 0.75), (1.75, 2.25)


# Define a Newton-Raphson method

# The derivative of the function
def dFdx(x):  
  return 2*x/(1+2*x**2+x**4) - 0.4

# Define the function for Newton-Raphson method
def NRroot(x,F,dFdx):
    for i in range(10):
        #Store the value of n
        n.append(i)
        y = x
        x = x - F(x)/dFdx(x)
        #Store the value of x_n
        x_n.append(x)
        z = x - y 
        #Store the value of x_n-x_n-1
        d.append(z)      
    return x

# Create a place to store values of n, x_n and the difference between x_n-x_(n-1), which we will call d. 
n = []
x_n = []
d = []

# Make an initial guess within the first range, (-0.25, 0.25)
a = NRroot(0, F, dFdx)

# Create arrays
n = np.array(n)
x_n = np.array(x_n)
d = np.array(d)

#print the values of n, x_n, and x_n-x_n-1 for this intial condition
print('For the initial guess x=0')
print('The values of n:', n)
print('The values of x_n:', x_n)
print('The values of x_n-x_n-1:', d)

#Recreate the empty sets
n = []
x_n = []
d = []

# Make an initial guess within the second range, (0.25, 0.75)
b = NRroot(0.5, F, dFdx)

# Create arrays
n = np.array(n)
x_n = np.array(x_n)
d = np.array(d)

#print the values of n, x_n, and x_n-x_n-1 for this intial condition
print('')
print('For the initial guess x=0.5')
print('The values of n:', n)
print('The values of x_n:', x_n)
print('The values of x_n-x_n-1:', d)

#Recreate the empty set
n = []
x_n = []
d = []

# Make an initial guess within the second range, (1.75, 2.25)
c = NRroot(2, F, dFdx)

# Create arrays
n = np.array(n)
x_n = np.array(x_n)
d = np.array(d)

#print the values of n, x_n, and x_n-x_n-1 for this intial condition
print('')
print('For the initial guess x=2')
print('The values of n:', n)
print('The values of x_n:', x_n)
print('The values of x_n-x_n-1:', d)

#print the roots given by the Newton-Raphson method
print('The roots are located at, roughly, ', a, ",", b, ",", c)

#check that the Newton-Raphson method has in fact converged on roots by putting the roots found back into the original function and checking they equate to approximately zero
print('If the Newton-Raphson method above has converged to a root, F(x) will be approximately equal to 0. If it is not, input alternative intial conditions')
print('F(a) is equal to ', F(a))
print('F(b) is equal to ', F(b))
print('F(c) is equal to ', F(c))
print('These are all either equal to zero or approximately equal to zero and so the sequence has converged to the roots of F(x)')


print('')
print('------------------------------------')
print('')

# 1b
# Import the python packages required
import matplotlib.pyplot as plt
import numpy as np

# Define the function in the question
def F(x, t):
    return 0.001 - 0.4*x + (x**2/(1+x**2))
    

# Now write a fourth order Runge-Kutta scheme to 
# integrate our function for a single time step:
def RK4step(x, t, h, F):
    k1 = h*F(x, t)
    k2 = h*F(x+k1/2.0, t+h/2.0)
    k3 = h*F(x+k2/2.0, t+h/2.0)
    k4 = h*F(x+k3, t+h)
    return x + (k1 + 2*k2 + 2*k3 + k4)/6

# To integrate the function (solve the ODE) choose a suitable time step h,
# and number of steps to take. The maximum time t reached will be h*nsteps

# Choice of timestep, h, and total number of steps to take
# This choice of h and nsteps means that the shape of the graph is shown and it extends roughly until it levels out
h = 0.1
nsteps = 400

# Also take an initial condition, here x(0)=0.45
x = 0.45
x1 = 0.5
t = 0.0

# Create arrays in which to store solutions
xstore = []
x1store = []
tstore = []
xstore.append(x)
x1store.append(x1)
tstore.append(t)

# Now solve the ODE using the Runge-Kutta method
for n in range(nsteps+1):
  x = RK4step(x, t, h, F)
  x1 = RK4step(x1, t, h, F)
  t = t+h
  xstore.append(x)
  x1store.append(x1)
  tstore.append(t)
  
# Plot the results  
plt.plot(tstore, xstore, label = 'x(0)=0.45')
plt.plot(tstore, x1store, label = 'x(0)=0.5')
plt.xlabel('t')
plt.ylabel('x')
plt.title('x(t) for x(0)=0.45, and x(0)=0.5')
plt.legend()
plt.show()


print('')
print('------------------------------------')
print('')

# Part 2: Helper functions

# 2a

#imprt the required packages
import matplotlib.pyplot as plt
import numpy as np

# We have the following coupled system:
# dx/dt = x*(1-x-0.1exp(0.1y))
# dy/dt = y*(1-y-0.2exp(0.3x))

# Define this as a vector valued function:
def f(x,y):
    return np.array([x*(1-x-0.1*np.exp(0.1*y)), y*(1-y-0.2*np.exp(0.3*x))])

# Define the functions to generate the x_n+1 and y_n+1 values. These have been derived on paper analytically using the formulas from the lecture notes

# The function which generates the x-value
def g(x, y):
    return -2*(x**2)*y - 0.2*np.exp(0.3*x)*(x**2) + 0.01*np.exp(0.1*y)*x*(y**2) + 2*x*y - 0.21*np.exp(0.1*y)*x*y + 0.002*np.exp(0.3*x + 0.1*y)*x*y + x + 0.2*np.exp(0.3*x)*x - 0.02*np.exp(0.3*x + 0.1*y)*x

# The function which generates the y-value
def h(x, y):
    return -2*(y**2)*x - 0.1*np.exp(0.1*y)*(y**2) + 0.06*np.exp(0.3*x)*y*(x**2) + 2*x*y - 0.46*np.exp(0.3*x)*x*y + 0.006*np.exp(0.3*x + 0.1*y)*x*y + y + 0.1*np.exp(0.1*y)*y - 0.02*np.exp(0.3*x + 0.1*y)*y

# Create the 2-D Newton-Raphson method
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

# Print the found steady states
print('The steady states are:')
print(W1,W2,W3,W4)

#To check, f(x, y) should be very close to [0,0]  
print('The value of f(W4) is', f(W4[0], W4[1]), '. This is very close to [0, 0], showing that this is in fact a steady state.')

print('')
print('------------------------------------')
print('')

# Part 2b

#Import the required package
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

#To generate a nice looking phase plane plot I have generated a lots of intial conditions and made it such that they all come from the edge of the region displayed so that the look of the graph is most clear
#Having such a large i does not take significant computing time and so I think it is viable
for i in range(200):
    #This section ensures that the initial conditions are randomly assignedto each side along the edges of the region graphed
    s = random.randint(0, 3)
    if s == 3:
        #This is the low x region
        x = random.randint(1,10)/100
        y = random.randint(0,200)/100
    elif s == 2:
        #This is the high x region
        x = 2
        y = random.randint(0,200)/100
    elif s == 1:
        #This is the low y region
        x = random.randint(0,200)/100
        y = random.randint(1,10)/100
    else:
        #This is the high y region
        x = random.randint(0,200)/100
        y = 2
        
    #Define t as 0
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
    
#Plot the critical points
X = np.array([W1[0], W2[0], W3[0], W4[0]])
Y = np.array([W1[1], W2[1], W3[1], W4[1]])

# Make a plot of this solution
plt.scatter(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solutions to the ODE')
plt.xlim(0,2)
plt.ylim(0,2)






