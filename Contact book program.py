# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:15:03 2021

@author: micha
"""

names = []
numbers = []

a = 0
while a == 0:
    ent = input("How many phone numbers would you like to save? ")

    try:
        num = int(ent)
    except:
        num = -1
        
    if num > 0:
        a = 1
    else:
        print("Please enter a positive integer")
        
for i in range(num):
    name = input("Please enter the name of a contact: ")
    names.append(name)
    a = 0
    while a == 0:
        number = input("Please enter the phone number of the contact: ")
        if len(number) == 11:
            numbers.append(number)
            a = 1
        else:
            print("That is not a valid phone number")
        
print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], numbers[i]))


finder = input("Please type the name of the contact who's information you would like to find: ")

b = 0
while b == 0:
    for i in range(len(names)):
        if names[i] == finder:
            print(name, ":", number)
            b = 1
        elif i == (len(names)-1):
            print("There are no names in your contact book matching this")
            b = 1
            

































