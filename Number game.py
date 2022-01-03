# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:03:13 2021

@author: micha
"""

#Number game

import numpy as np
import random 

points = 0
b = 40
while b == 40:
    print("Rules: You will have three tries to guess each number within a range of your choice. There will be a maximum of three points avaliable which goes down to zero if you cannot guess the number within the avaliable guesses. Each failed guess will reveal a clue about the number generated.")
    a = 10
    while a == 10:
        ran = input('Please enter a positive integer as the range for the game:')
        try:
            iran = int(ran)
        except:
            iran = -1
                
        if iran > 10:
            a = 20
            if iran < 20:
                print('Pretty low range, smells like bitch in here...')
            elif iran < 75:
                print('Acceptable range. Not to small but clearly not ready to play with the big boys yet')
            else:
                print('Okay big man, lets see if you are really all that.')
        elif iran <= 10:
            if iran > 0:
                print("Don't be a punk ass bitch, pick a higher number you little coward")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            else:
                print("That range doesn't work, please pick a positive integer")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    val = int(random.randint(0, iran))



    guess_1 = input('Please make an initial guess:')
    guess_1 = int(guess_1)
    if guess_1 == val:
        print('Holy crap! Your powers of guessing are elite! You have won three points!')
        points = points + 3
    else:
        print('Unlucky mate. Time for your first clue then I guess.')
    
    if guess_1 > val:
        print('Your guess was larger than the value you search for')
    else:
        print('Your guess was smaller than the value you search for')




    guess_2 = input('Please make a second guess:')
    guess_2 = int(guess_2)
    if guess_2 == val:
        print('Holy crap! Your powers of guessing are elite! You have won two points!')
        points = points + 2
    else:
        print('Unlucky mate. Time for your second clue then I guess.')
    
    if guess_2 > val:
        print('Your guess was larger than the value you search for')
    else:
        print('Your guess was smaller than the value you search for')
    
    
    
    div = int(val/2)
    
    if div == int((val-1)/2):
        print('Also, the number you are looking for is odd')
    else:
        print('Also, the number you are looking for is even')
    
    print(val)




    guess_3 = input('Please make a final guess:')
    guess_3 = int(guess_3)
    if guess_3 == val:
        print('Holy crap! Your powers of guessing are elite! You have won one points, just in time!')
        points = points + 1
    else:
        print('Unluckyyyyyyy. No points for you in that case...')
    



    while a == 20:
        question = input('Would you like to play again(Yes/No)?')
        if question == 'Yes':
            a = 30
            print('Okay here we go')
        elif question == 'No':
            b = 50
            a = 30
            print("Great! It has been a pleasure playing with you, you have won ", points, " points!")
        else:
            print('Please answer Yes or No.')

