# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:46:29 2021

@author: micha
"""
#Coding lessons for Python

x = 1
#Assignment statement
print(x)
#Assigns x a value and prints it to the console

x = x + 1
#Assignment with expression
print(x)
#Assigns a new value of x (ammended) and prints it to the console

#Reserved words: Words with a pre-assigned meaning
#These include:
False
#Not true
None 
True 
#Not false
and
as
assert
break
class
if
#Asks whether a condition is met and reacts based on the True or False
def
#Defines a function
del
elif
#Adds further conditions to the if statement
else
#If the if condition is not met, this instructs the programme what to do now
except
#Used as part of the try function for if the try does not in face work
return 
#Finishes an instruction, gives an output
for
from
global
try
#Put around a dangerous piece of code, if it works, except is skipped, however, it will jump to the except section if the try fails
import
in
is
#Similar to equal to but more stringent 
lambda
while
#Repeats the process until a given condition is not met
not
or
pass
raise
finally
continue
#Stops that iteration and restarts
nonlocal
with
yield

#Constants = a fixed value that can be numbers, letters, or even a string

#Variables = a named place in the memory where a programmer can store data and later retrieve it using the variable name
#Variables: must start with a letter or underscore; must consist of letters, numbers, and underscores; are case sensitive

#Float is a number with a decimal
#All divisions of integers will result in a float

nam = input("Who are you? ")
print("Hello", nam)
how = input("How are you today? ")
print("That's great to hear.")

<>#Greater or lesser than
<=, >= #Less than or equal to, greater than or equal to
==#Equal to
!=#Not equal to

#Examples of the try function
astr = 'Hello Michael'
try:
    istr = int(astr)
except:
    istr = -1
    
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
    
print('Second', istr)

#To detect correct type of input
a = 10

while a==10:
    rawstr = input('Enter a positive number: ')
    try:
        ival = int(rawstr)
    except:
        ival = -1
    
    if ival > 0:
        a=20
        print('Nice work')
    else:
        print('Not a positive number. Please try again.')

#Repeats what you say until you say done, or if you start a line with a # sign
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'Done':
        break
    print(line)
print('Done!')


things = [4, 4, 4, 4, 4, 4, 4, 9994, 120, 450, 450, 450, 450, 7.6, 0.24, 33, 99]

#Finds the largest number in array
def Max(x):
    largest_so_far = x[0]
    for thing in x:
        if thing > largest_so_far:
            largest_so_far = thing
    return largest_so_far

#Finds smallest number in array
def Min(x):
    smallest_so_far = x[0]
    for thing in x:
        if thing < smallest_so_far:
            smallest_so_far = thing
    return smallest_so_far

#Finds the number of datapoints
def Count(x):
    count = 0
    for thing in x:
        count = count + 1
    return count

#Finding the mode
def Mode(x):
    number_of_repeats = []
    for i in range(Count(x)):
        count = 0
        for j in range(i, Count(x)):
                if x[i] == x[j]:
                    count = count + 1
                    number_of_repeats.insert(i, count)
    most_repeated = Max(number_of_repeats)
    for k in range(Count(x)):
        if number_of_repeats[k] == most_repeated:
            return x[k]

#First letter is 0 and it goes up to the second number minus 1
s = 'Michael Stanway'
print(s[0:4])

#Converts to lower case
print('Hi There'.lower())

#Finds things in strings
print('Hi There'.find('h'))

#To replace
print('Hi There'.replace('e', 'x'))
print('Hi There'.replace('There', 'Michael'))

#Gets rid of white space (left, right, all)
lstrip()
rstrip()
strip()

print('       Hi There'.lstrip())

#Tells us what something starts with (True or false)
.startswith('')

#Open and use files
fhand = open(filename, mode)
#Filename is a string, mode is optional and should be r to read the file and w to write to the file

#Prints file
fhand = open(filename)
print(fhand)

#\n indicates a new line

#Prints each line in a text file (cheese essentially means line)
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

#Prints all senders
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#Skips all lines not refering to senders by skipping lines
fhand = open('mbox.txt')
for line in fhand:
    line = line.lstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#Finds the number of senders in a file
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    count = 0
    for line in fhand:
        line = line.lstrip()
        if line.startswith('From:'):
            count = count + 1
    print('There were', count, 'senders attatched in', fname)
except:
    print('There is no file under that name')

#Items within lists can be changed
lotto = [1, 2, 2, 4, 5]
sum(lotto)
print(lotto)
lotto[2] = 3
print(lotto)
print('Thats how to count you fricking idiot')

#LISTS
append
#Adds something to a list
count
extend
index
insert
pop
remove
reverse
sort
#sorts the list in some way
split
#Breaks up a line into a list, you can tell it which character to take as the delineator
len()
#Finds the length of something (strings and lists)
max()
#Finds the largest value
min()
#Finds smallest value
sum()
#Finds the sum of a list

stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)


things = [4, 4, 4, 4, 4, 4, 4, 9994, 120, 450, 450, 450, 450, 7.6, 0.24, 33, 99]
things.sort()
print(things)

numlist = list()
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    value = float(value)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('The average of this list is ', average)

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
email = words[1]
pieces = email.split('@')
print(pieces[1])

#DICTIONARIES
purse = dict()
purse['money'] = 123
purse['candy'] = 12
purse['tissues'] = 13
print(purse)
print(purse['candy'])
purse['money'] = purse['candy'] + 4
print(purse)

#To find the most common name
counts = dict()
names = ['Michael', 'Michael', 'Michael', 'Michael', 'Michael', 'Michael', 'Lucy', 'Lucy', 'Lucy', 'Mum', 'Mum', 'Mum', 'Mum', 'Mum']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#Dictionary idiom (equivalent to above)
counts = dict()
names = ['Michael', 'Michael', 'Michael', 'Michael', 'Michael', 'Michael', 'Lucy', 'Lucy', 'Lucy', 'Mum', 'Mum', 'Mum', 'Mum', 'Mum']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
#Get essentially does the above

#Prints the keys and values
print(counts.items())

#Finding the mode
def Mode(x):
    number_of_repeats = []
    for i in range(Count(x)):
        count = 0
        for j in range(i, Count(x)):
                if x[i] == x[j]:
                    count = count + 1
                    number_of_repeats.insert(i, count)
    most_repeated = Max(number_of_repeats)
    for k in range(Count(x)):
        if number_of_repeats[k] == most_repeated:
            return x[k]

#Finds the largest number in array
def Max(x):
    largest_so_far = x[0]
    for thing in x:
        if thing > largest_so_far:
            largest_so_far = thing
    return largest_so_far

#Finds smallest number in array
def Min(x):
    smallest_so_far = x[0]
    for thing in x:
        if thing < smallest_so_far:
            smallest_so_far = thing
    return smallest_so_far

#Finds the number of datapoints
def Count(x):
    count = 0
    for thing in x:
        count = count + 1
    return count



fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mbox1.txt'
hand = open(fname)


di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    Wds = lin.split()
    #print(wds)    
    for w in wds:
        w = w.lower()
        di[w] = di.get(w, 0) + 1
        #print(w, di[w])

print(di)

#Tuples are immutable
#You can also store variables in them

(x, y) = (4, 'Fred')
print(x)
print(y)

[x, y] = ['George', 99]
print(x)
print(y)

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
#Prints (k, v)

#When tuples are compared they take only the first discrepancy

items()
#Turns the values in a dictionary into tuples in a list
sorted()
#Sorts the tuples in the dictionary

di = {'a': 10, 'b':1, 'c':22}
itm = list()
for (k, v) in di.items():
    itm.append((v, k))
mod = sorted(itm, reverse = True)
print(mod)

di = {'a': 10, 'b':1, 'c':22}
print(sorted([(v, k) for k, v in di.items()], reverse = True))



fname = input('Enter file: ')
if len(fname) < 1 : fname = 'mbox1.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)    
    for w in wds:
        w = w.lower()
        di[w] = di.get(w, 0) + 1
        #print(w, di[w])

#print(di)
ord = sorted([(v, k) for k, v in di.items()], reverse = True)
for v, k in ord[:5]:
    print(k, v)

#Regular expression
import re

^
#Matches the beginning of a line
$
#Matches the end of a line
.
#Matches any character
\s
#Matches whitespace
\S
#Matches any non-whitespace character
*
#Repeats a character zero or more times
*?
#Repeats a character zero or more times (non-greedy)
+
#Repeats a character one or more times
+?
#Repeats a character one or more times (non-greedy)
[aeiou]
#Matches a listed character in the listed set
[^XYZ]
#Matches a listed character not in the listed set

[a-z0-9]
#The set of characters can include a range
(
#Indicates where string extraction is to start 
)
#Indicates where string extraction is to end

import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
z = re.findall('[a-z]+', x)
print(z)

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

import socket
telnet www.dr-chuck.com 80
GET http://www.dr-chuck.com/page1.htm HTTP/1.0











































