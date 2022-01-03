# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:14:56 2020

@author: michael
"""
#Hello Python I'm home, time for worksheet 2

#Question 1
x=10
y=100

x=y
y=y//10

print(x)
print(y)

#Question2
z="Hello my name is "

m="Michael"

g=z+m

s=z[0:6]+m

print(z)
print(m)
print(g)
print(s)

#Question 3
s1="4"
s2="2"
f1=4.0
f2=2.0
i1=4
i2=2
s1+s2
#answer is '42'

i1*s1
#answer is '4444'

i2/i1
#answer is 0.5

i2//i1
#answer is 0

f1/f2
#answer is 2.0

f1/i2
#answer is 2.0

(f1+i2)/i2
#answer is 3.0

#s1/f2
#results in error as they are the wrong type

#Question 4
s = "Maths"
n = 5
print(s[n//2]) #Added a forward slash so that the integer value would be taken

#Mathematics section
#Question 1
from numpy import *
r = 2
d = 2*r
c = pi*d
a = pi*r**2

print(d)
print(c)
print(a)

r = 4
d = 2*r
c = pi*d
a = pi*r**2

print(d)
print(c)
print(a)

r = 6
d = 2*r
c = pi*d
a = pi*r**2

print(d)
print(c)
print(a)

#Question 2
x = 1
y = 2

r = sqrt(x**2 + y**2)
t = arctan(y/x)

print(r)
print(t)

x = 0.1
y = -5.6

r = sqrt(x**2 + y**2)
t = arctan(y/x)

print(r)
print(t)

x = -2.32
y = -1.03

r = sqrt(x**2 + y**2)
t = arctan(y/x)

print(r)
print(t)

#Question 3
height_metric = 1.90
height_cm = 100 * height_metric
cm_to_inch = 0.39379
height_inches = height_cm * cm_to_inch
number_feet = height_inches // 12
number_inches = int(round(height_inches - number_feet * 12, 0))
print(height_metric, "metres is", number_feet, "ft", number_inches, "in")

#Optional questions
#Question 1
from numpy import *
a = 2.0
b = 5.0
c = sqrt(5) - 1.0

x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)

gradf1 = 2 * x1 + 3
gradf2 = 2 * x2 + 3
gradg1 = -2 * x1 - 2
gradg2 = -2 * x2 - 2

print("Intersections at points:")
print("(x1,y1) = ", x1, x1 ** 2 + 3 * x1 + sqrt(5))
print("(x2,y2) = ", x2, x2 ** 2 + 3 * x2 + sqrt(5))

print("Gradients at those points:")
print("Point (x1,y1):")
print("Gradient of tangent to f(x) = ", gradf1)
print("Gradient of tangent to g(x) = ", gradg1)
print("Point (x2,y2):")
print("Gradient of tangent to f(x) = ", gradf2)
print("Gradient of tangent to g(x) = ", gradg2)

#Question 2
min(2.1,4.2,3.0,113.2)
max(2.1,4.2,3.0,113.2)
#Gives the minimum and maximum value in the list respectively

statement_Balance = 500
f = min(statement_Balance, 5) 
minimum_Payment = max(f, statement_Balance*0.03)
print(minimum_Payment)

statement_Balance = 100
f = min(statement_Balance, 5) 
minimum_Payment = max(f, statement_Balance*0.03)
print(minimum_Payment)

statement_Balance = 4
f = min(statement_Balance, 5) 
minimum_Payment = max(f, statement_Balance*0.03)
print(minimum_Payment)