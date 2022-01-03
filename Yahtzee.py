# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:01:27 2021

@author: micha
"""

#Yahtzee!
import random

score = {"1's": 0, "2's": 0, "3's": 0, "4's": 0, "5's": 0, "6's": 0, "Three of a kind": 0, "Four of a kind": 0, "Low Straight": 0, "High Straight": 0, "Fullhouse": 0, "Chance": 0, "Under 8's": 0, "Yahtzee": 0}

def roll_dice(x):
    dice_list = []
    for i in range(x):
        roll = random. randint(1, 6)
        dice_list.append(roll)
    return dice_list

def check_number(x, y):
    counts = dict()
    counts[y] = 0
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    if counts[y] == 0:
        include_number = False
    else:
        include_number = True
    
    return include_number

def check_threeofakind(x):
    counts = dict()
    threeofakind = False
    val = -1
    a = 0
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    length = len(counts)
    while threeofakind == False and a <= length:
        for (k, v) in counts.items():
            if v >= 3:
                threeofakind = True
                val = k 
            else:
                a = a + 1
    return threeofakind
    
def check_fourofakind(x):
    counts = dict()
    fourofakind = False
    val = -1
    a = 0
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    length = len(counts)
    while fourofakind == False and a <= length:
        for (k, v) in counts.items():
            if v >= 4:
                fourofakind = True
                val = k 
            else:
                a = a + 1
    return fourofakind


def check_yahtzee(x):
    counts = dict()
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    for place in counts:
        if counts[place] == 5:
            yahtzee = True
        else:
            yahtzee = False
    return yahtzee
    

def check_under8(x):
    tot = sum(x)
    if tot < 8:
        under_8 = True
    else:
        under_8 = False
    return under_8
    
def check_fullhouse(x):
    counts = dict()
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    length = len(counts)
    if length == 2:
        four = check_fourofakind(x)
        if four == True:
            fullhouse = False
        else:
            fullhouse = True
    else:
        fullhouse = False
    return fullhouse
    
def check_highstraight(x):
    counts = dict()
    highstraight = False
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    length = len(counts)
    if length == 5:
        ord_counts = sorted(counts)
        if ord_counts == [1, 2, 3, 4, 5]:
            highstraight = True
        elif ord_counts == [2, 3, 4, 5, 6]:
            highstraight = True
        else:
            highstraight = False
    return highstraight

def check_lowstraight(x):
    counts = dict()
    lowstraight = False
    for number in x:
        counts[number] = counts.get(number, 0) + 1
    length = len(counts)
    if length >= 4:
        ord_counts = sorted(counts)
        if ord_counts[:4] == [1, 2, 3, 4]:
            lowstraight = True
        elif ord_counts[:4] == [2, 3, 4, 5]:
            lowstraight = True
        elif ord_counts[:4] == [3, 4, 5, 6]:
            lowstraight = True
        elif ord_counts[1:5] == [3, 4, 5, 6]:
            lowstraight = True
        else:
            lowstraight = False
    return lowstraight

def roll_checker(x):
    a = 0
    while a == 0:
        kept_roll = input("Please select the numbers that you would like to keep (in the form n n n where n is each a number to keep, type 0 if you want a complete reroll): ")
        kept_numbers = kept_roll.split()        
        back_up = list()
        if kept_numbers == ['0']:
            print("You have chosen to roll all dice again")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            kept_numbers = []
            a = 1
            return kept_numbers
        else:
            for i in range(len(kept_numbers)):
                z = kept_numbers[i]
                z = int(z)
                kept_numbers[i] = z
                
            for i in range(len(kept_numbers)):
                z = kept_numbers[i]
                check_roll = x
                try:
                    check_roll.remove(z)
                    back_up.append(z)
                    if i == (len(kept_numbers)-1):
                        a = 1
                except:
                    for number in back_up:
                        check_roll.append(number)
                    print(check_roll)
                    print("Please select numbers within your roll")
                    break
    
            print("The numbers you have chosen to keep are", kept_numbers)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return kept_numbers

def score_upload(x):
    print("These are the numbers to type for each place to upload your score: 1. 1's, 2. 2's, 3. 3's, 4. 4's, 5. 5's, 6. 6's, 7. Three of a kind, 8. Four of a kind, 9. Low Straight, 10. High Straight, 11. Fullhouse, 12. Chance, 13. Under 8's, 14. Yahtzee. Please select the number of the place you would like to put your score: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    a = 0
    di = dict()
    for number in x:
        di[number] = di.get(number, 0) + 1
    while a == 0:
        place = input("Where would you like to upload your score?")
        place = int(place)
        if place == 1:
            if score["1's"] == 0:
                if check_yahtzee(x) == True:
                    score["1's"] = 50
                    a = 1
                elif check_number(x, 1) == True:
                    y = place*di[1]
                    score["1's"] = y
                    a = 1
                else:
                    print("There are no 1's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 2:
            if score["2's"] == 0:
                if check_yahtzee(x) == True:
                    score["2's"] = 50
                    a = 1
                elif check_number(x, 2) == True:
                    y = place*di[2]
                    score["2's"] = y
                    a = 1
                else:
                    print("There are no 2's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 3:
            if score["3's"] == 0:
                if check_yahtzee(x) == True:
                    score["3's"] = 50
                    a = 1
                elif check_number(x, 3) == True:
                    y = place*di[3]
                    score["3's"] = y
                    a = 1
                else:
                    print("There are no 3's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 4:
            if score["4's"] == 0:
                if check_yahtzee(x) == True:
                    score["4's"] = 50
                    a = 1
                elif check_number(x, 4) == True:
                    y = place*di[4]
                    score["4's"] = y
                    a = 1
                else:
                    print("There are no 4's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 5:
            if score["5's"] == 0:
                if check_yahtzee(x) == True:
                    score["5's"] = 50
                    a = 1
                elif check_number(x, 5) == True:
                    y = place*di[5]
                    score["5's"] = y
                    a = 1
                else:
                    print("There are no 5's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 6:
            if score["6's"] == 0:
                if check_yahtzee(x) == True:
                    score["6's"] = 50
                    a = 1
                elif check_number(x, 6) == True:
                    y = place*di[6]
                    score["6's"] = y
                    a = 1
                else:
                    print("There are no 6's in your roll. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 7:
            if score["Three of a kind"] == 0:
                if check_yahtzee(x) == True:
                    score["Three of a kind"] = 50
                    a = 1
                elif check_threeofakind(x) == True:
                    score["Three of a kind"] = 15
                    a = 1
                else:
                    print("You don't have a three of a kind. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 8:
            if score["Four of a kind"] == 0:
                if check_yahtzee(x) == True:
                    score["Four of a kind"] = 50
                    a = 1
                elif check_fourofakind(x) == True:
                    score["Four of a kind"] = 20
                    a = 1
                else:
                    print("You don't have a four of a kind. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 9:
            if score["Low Straight"] == 0:
                if check_yahtzee(x) == True:
                    score["Low Straight"] = 50
                    a = 1
                elif check_lowstraight(x) == True:
                    score["Low Straight"] = 25
                    a = 1
                else:
                    print("You don't have a low straight. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 10:
            if score["High Straight"] == 0:
                if check_yahtzee(x) == True:
                    score["High Straight"] = 50
                    a = 1
                elif check_highstraight(x) == True:
                    score["High Straight"] = 30
                    a = 1
                else:
                    print("You don't have a high straight. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 11:
            if score["Fullhouse"] == 0:
                if check_yahtzee(x) == True:
                    score["Fullhouse"] = 50
                    a = 1
                elif check_fullhouse(x) == True:
                    score["Fullhouse"] = 35
                    a = 1
                else:
                    print("You don't have a fullhouse. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 12:
            if score["Chance"] == 0:
                if check_yahtzee(x) == True:
                    score["Under 8's"] = 50
                    a = 1
                else:
                    score["Chance"] = sum(x)
                    a = 1
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 13:
            if score["Under 8's"] == 0:
                if check_yahtzee(x) == True:
                    score["Under 8's"] = 50
                    a = 1
                elif check_under8(x) == True:
                    score["Under 8's"] = 40
                    a = 1
                else:
                    print("You don't have an under 8. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        elif place == 14:
            if score["Yahtzee"] == 0:
                if check_yahtzee(x) == True:
                    score["Yahtzee"] = 50
                    a = 1
                else:
                    print("You don't have a yahtzee. Please choose somewhere else to put your score.")
            else:
                print("There is already a score in this section. Please choose somewhere else to put your score")
        else:
            print("That number is not an option, please choose one from the list.")
    return score

def check_any(x):
    truth_check = {"1's": check_number(x, 1), "2's": check_number(x, 2), "3's": check_number(x, 3), "4's": check_number(x, 4), "5's": check_number(x, 5), "6's": check_number(x, 6), "Three of a kind": check_threeofakind(x), "Four of a kind": check_fourofakind(x), "Low Straight": check_lowstraight(x), "High Straight": check_highstraight(x), "Fullhouse": check_fullhouse(x), "Chance": True, "Under 8's": check_under8(x), "Yahtzee": check_yahtzee(x)}
    truth_list = []
    for place in score:
        if score[place] == 0:
            truth_list.append(truth_check[place])
    di = {True:0, False:0}
    for val in truth_list:
        di[val] = di.get(val, 0) + 1
    if di[True] == 0:
        print("You have nowhere to put your points.")
        a = 0
        while a == 0:
            cut_off_str = input("Please select a category to cross (1. 1's, 2. 2's, 3. 3's, 4. 4's, 5. 5's, 6. 6's, 7. Three of a kind, 8. Four of a kind, 9. Low Straight, 10. High Straight, 11. Fullhouse, 12. Chance, 13. Under 8's, 14. Yahtzee. Please select the number of the place you would like to cross: ")
            cut_off = int(cut_off_str)
            if cut_off == 1:
                if score["1's"] == 0:
                    score["1's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 2:
                if score["2's"] == 0:
                    score["2's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 3:
                if score["3's"] == 0:
                    score["3's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")            
            elif cut_off == 4:
                if score["4's"] == 0:
                    score["4's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 5:
                if score["5's"] == 0:
                    score["5's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 6:
                if score["6's"] == 0:
                    score["6's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 7:
                if score["Three of a kind"] == 0:
                    score["Three of a kind"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 8:
                if score["Four of a kind"] == 0:
                    score["Four of a kind"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 9:
                if score["Low Straight"] == 0:
                    score["Low Straight"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 10:
                if score["High Straight"] == 0:
                    score["High Straight"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 11:
                if score["Fullhouse"] == 0:
                    score["Fullhouse"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 12:
                if score["Chance"] == 0:
                    score["Chance"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 13:
                if score["Under 8's"] == 0:
                    score["Under 8's"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            elif cut_off == 14:
                if score["Yahtzee"] == 0:
                    score["Yahtzee"] = -1
                    a = 1
                else:
                    print("There is a score here. Please choose somewhere else to cross")
            else:
                print("That is not an option please choose again.")
    else:
        score_upload(x)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     
               
def play_game(x):
    print("Hello", x, "it's time to play Yahtzee!")
    a = 0       
    while a == 0:
        first_roll = roll_dice(5)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your first roll is", first_roll)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        number_held = roll_checker(first_roll)
        if len(number_held) == 5:
            final_roll = number_held
            check_any(final_roll)
            for place in score:
                print(place, score[place])
        else:
            new_dice = roll_dice(5 - len(number_held))
            second_roll = new_dice + number_held
            print("Your second roll is", second_roll)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            number_held = roll_checker(second_roll)
    
            if len(number_held) == 5:
                final_roll = second_roll
                check_any(final_roll)
                for place in score:
                    print(place, score[place])
            else:
                new_dice = roll_dice(5 - len(number_held))
                final_roll = new_dice + number_held
                print("Your last roll is", final_roll)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                check_any(final_roll)
                for place in score:
                    print(place, score[place])
        
        b = 0
        for place in score:
            if score[place] == 0:
                b = b + 1
        if b == 0:
            final_score = 0
            print("Congratulations you have finished the game!")
            for place in score:
                if score[place] == -1:
                    score[place] = 0
                final_score = final_score + score[place]
            print("Your final score was", final_score)
            d = 0
            while d == 0:
                again = input("Would you like to play again(Y/N)?")
                if again == 'N':
                    print("Thank you for playing", x,", please have a good day.")
                    a = 1
                    d = 1
                elif again == 'Y':
                    print('Here we go again')
                    d = 1
                else:
                    print("Please choose Y or N")

x = input("Hello, what is your name? ")
play_game(x)
























