# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:20:46 2020

@author: micha
"""

#Hello Python I'm home, time for worksheet 5
#Question 1
from numpy import log as ln
from numpy import *
def f(x):
    g = sin(x)/(ln(cos(x+1)+1))
    return g

print(f(1.0))

#Question 2
def h(x, y, z):
    z = (x**2+y**2+z**2)/(x**3+y**3+z**3)
    return z

print(h(2, 3, 4))

#Quesiton 3
print("Please enter a real number")
x = float(input(">"))

if x==0:
    print("boring ass fool")
elif x>0:
    print("optomistic shit")
elif x<0:
    print("cheer up you wee bastard")

#Question 4
print("Please enter a natural number")
x = int(input(">"))
s=0

for m in range(x):
    s = s + m

print(s)    

#Mathematics Questions
#Question 1
from numpy import *
x=1
m=0

while m<25:
    print(x)
    print(x-sqrt(2))
    g = x - sqrt(2)
    if g<1*10**-14:
        print(m)
    x = 1 + 1/(1+x)
    m = m + 1
    
#Question 2
from numpy import *

N = 5.0
print("What number would you like to choose")
S = input("Number: ")
m = 0

def f(S, xn):
    g = 0.5*(x+S/xn)
    return g

x = 4.0
while m<N:
    x = f(S, x)
    m = m+1
    
print(x)
print(x/sqrt(15))
    


# the value of the iterate x[i] (we'll iterate in a loop later)
def f(S, xn):
    g = 0.5 * (x + S / xn)
    return g


# Now lets use the function in a for loop to do the iteration:

# Number to take the square root of
S = 15.0

# Initial guess for the root.
# Doesn't matter too much what we choose. (Try it.)
x = 4.0

# Number of iterations to use.
N = 5

# Now carry out the iteration
for i in range(0, N, 1):
    x = f(S, x)
    # Have a look at the iterates while we're going
    print(x)
    # But for a large number of iterations prob. comment that out!

# Let the user know the result
print("after", N, "iterations we approximate sqrt(", S, ")=", x)
print("while sqrt(", S, ")is", sqrt(S), "to 11 d.p.")
print("the error is", x - sqrt(S))


#Question 3
from numpy import *

def f(x):
    b = x**2 + 3*x + 3
    return b
def g(x):
    c = sin(x) + 2*(x - 2)/(x + 1)
    return c
def h(x):
    a = sinh(x + 1) - e**2*x
    return a

g(f(5))

g(h(5))

f(g(2.1))

h(g(f(2*pi)))
    













