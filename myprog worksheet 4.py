# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:34:16 2020

@author: micha
"""

#Hello Python I'm home, time for worksheet 4

#Question 1
x = 9
y = 1.2

print(x>y)

if x>y:
    print(x, " is greater than ", y)
else:
    print(x, " is less than or equal to ", y)

#Question 2
m = 0

while m<21:
    print(m**2)
    m = m+1
    
n = 123212434
count = 0

while n>1:
    print(n)
    n = n/2
    count = count + 1
    
print(count)

#Question 3
for m in range (101):
    j = m%7
    if j==0:
        print(m, "we got one boys")
    
b = 0
m = 0

while b<22:
    j = m%7
    if j==0:
        b = b+1
        print(m, "we got one boys")
    m = m+1
    
#Mathematics Questions
#Question 1
from numpy import *

N = 500
s = 0

for m in range(N):
    term = 1/(2*(m+1)-1)
    z = m%2
    if z==0:
        s = s+term
    else:
        s = s-term

print(s)
print(s/(pi/4))

#Question 2
a = 3
r = 1.1
s = 0
m = 0

while s<10000:
    term = a*r**m
    s = s + term
    m = m+1
    
print(m+1)

#Optional Questions
#Question 1
N = 1000
s = 0

for m in range(N):
    j = m%3
    k = m%5
    if (j or k) == True:
        s = s + m
        
print(s)

#Question 2
s = 0
t = 1
e = 0

while t<100:
    t = s + t
    s = t - s
    z = t%2
    if z==0:
        e = e+
        t
        
print(e)