# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:01:54 2020

@author: micha
"""

#Hello Python I'm home, time for worksheet 2

#Question 1
for x in range(1000,1016,1):
    print(x)
    
#Question 2
for x in range(100,201,2):
    print(x," squared is ", x**2)

#Question 3
N = 6

s = 1

for m in range(N):
    term = m+1
    s = s*term
    
print(N," factorial is ", s)

N = 600

s = 1

for m in range(N):
    term = m+1
    s = s*term
    
print(N," factorial is ", s)

#Question 4
N = 100

s = 0

for m in range(N):
    term = m+1
    s = s+term
    
print("The sum of positive integers up to ",N, " is ", s)

#Question 5
N = 10

s = 0

for m in range(N):
    term = m**2+1
    s = s + term

print(s)

#Mathematics questions
#Question 1
N = 25
a = 3
r = 2
s = 0

for m in range(N):
    term = a*r**m
    s = s+term
    
print(s)

#Question 2
from numpy import *
N = 199
s = 0

for m in range(N):
    term = 1/((m+1)**2)
    s = s+term
    
print(s)
print(s/((pi**2)/6))
print("This is a good approximation of pi^2/6")

#Question 3
N = 10
s = 0
x = 3.4

for m in range(N):
    term = x**m/math.factorial(m)
    s = s+term
    
print(s)
print(s/exp(3.4))
#N = 100 provides a comparison of 1.0

#Optional Questions
#Question 1
N = 20
s = 0

for m in range(N):
    term = m/math.factorial(m+1)
    print(s+term)    
    s = s+term

print(s)

#Limit is 1






