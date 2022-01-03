# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:58:53 2021

@author: micha
"""



def prime_generator(x):
    a = 1
    #print(2)
    #print(3)
    #print(5)
    #print(7)
    #print(11)
    primes = [2, 3, 5, 7, 11]
    while a < x:
        c = {'0':0}
        if a <= 2 or a%2 == 1 and a%3 != 0 and a%5 != 0 and a%7 != 0 and a%11 != 0:
            b = int(a/13)
            for i in range(b+1):
                if i > 0:
                    d = str(int(a%i))
                    c[d] = c.get(d, 0) + 1
            if c['0'] == 1:
                #print(a)
                primes.append(a)
        a = a + 1
    return primes
    
#prime_generator(10000)

def prime_creator(x):
    a = x
    b = 0
    if a%2 == 0:
        a = a + 1
    while b == 0:
        c = {'0':0}
        for i in range(int(a/3)+1):
            if i > 0:
                d = str(int(a%i))
                c[d] = c.get(d, 0) + 1
        if c['0'] == 1:
            print(a)
            b = 1
        else:
            a = a + 1
        

#prime_creator(10000000)

def prime_checker(x):
    c = {'0':0}
    for i in range(int(x/2)+1):
        if i > 0:
            d = str(int(x%i))
            c[d] = c.get(d, 0) + 1
    if c['0'] == 1:
        #print(x, 'is a prime number')
        return True
    else:
        #print(x, 'is not a prime number')
        return False
    #Can be far more efficient
#prime_checker(9964324)
    
def prime_factor_decomposition(x):
    prime_list = prime_generator(x)
    a = x
    factors = []
    while prime_checker(a) == False:
        for prime in prime_list:
            if a%prime == 0:
                factors.append(prime)
                a = a/prime
    factors.append(int(a))
    return factors

print(sorted(prime_factor_decomposition(2354)))
    
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    