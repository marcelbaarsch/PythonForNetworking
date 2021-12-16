#!/usr/bin/env python3
# Lab 4 – Lists and list processing, logical and bitwise operations.
# Marcel Baarsch - marcelbaarsch@gmail.com

# import pdb

# Print prime numbers between a provided range
def step1():
    start = int(input("Please enter a Starting Integer: "))
    end = int(input("Please enter an Ending Integer: "))

    for x in range (start, end+1, 1):
        if x > 1:
            for y in range (2, x, 1):
                if x % y == 0:
                    break
            else:
                print (x)

# check if an inputted number is Prime
def step2():
    num = int(input("Please enter a number: "))

    if num > 1:
        for x in range (2, num // 2, 1):
            if num % x == 0:
                print (f'{num} is NOT Prime.')
                break
        else:
            print(f'{num} is Prime.')
    else:
        print(f'{num} is NOT Prime.')


# accept a word from the user and output the word if it's a Palindrome
def step3():

    word = input("Please enter a word: ")

    rev = ''

    for x in reversed(word):
        rev += x

    if word.lower() == rev.lower():
        print (f'{word} is a Palindrome.')
    else:
        print (f'{word} is not a Palindrome.')

# split the bits of an entered Binar number into a list
def step4():
    bStr = input("Please enter a Binary Number: ")

    bList = []

    for char in bStr:
        bList.append(char)

    print(f'The {bStr} as a Python List\n{bList}')

# Given an IPv4 address, split the characters of the string into a list of 4 octets
def step5():
    addy = input('IPv4 Address: ')

    octets = []
    temp = ''
    for letter in addy:
        if letter != '.':
            temp += str(letter)
        elif letter == '.':
            octets.append(temp)
            temp = ''
    else:
        octets.append(temp)
            
    print(f'as a list: {octets}')

# ... the instructions don't even make sense to me right now
def step6():
    Powersof2 = []

    for x in range(7,-1,-1):
        # print (x)
        Powersof2.append(2**x)

    binary = input('Please enter an 8-bit Binary Number: ')

    dec = 0
    index = 0

    for digit in binary:
        dec += int(digit) * Powersof2[index]
        index += 1

    print (f'In Decimal: {dec}')

# Lists and Slices
def step7():
    cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    print (cards)

    num = int(input("Number of cards for this cut: "))

    if num > len(cards):
        print(f'Number needs to be between 1 and {len(cards)}')
    else:
        print(f'Your cards cut at card {num} would look like this: {cards[:num]}')

# convert from 24 hour to 12 hour time format
def step8():
    time24 = input("Please enter a time in 24 hour format (hh:mm): ")

    if int(time24[:2]) > 12:
        time12 = str(int(time24[:2]) - 12)
        time12 += time24[2:5] + " PM"
        
    elif int(time24[:2]) == 12:
        time12 = time24 + " PM"

    else:
        time12 = time24 + " AM"

    print(time12)

# challenge: Bubble sort 2D list
def step9():
    colors = [['Yellow',3], ['Violet',6], ['Red',1], ['Blue',5], ['Orange',2], ['Green',4]]
    print (colors)

    for i in range(len(colors)-1):
        
        for x in range(0, len(colors)-i-1):
            
            if colors[x][1] > colors[x+1][1]:
            
                #swap
                colors[x][1], colors[x+1][1] = colors[x+1][1], colors[x][1]
                
    print (colors)

# CHALLENGE (OPTIONAL)
def step10():
    valid = ["0","1"]


print("Step 1:\n\n\n")
step1()

print("\n\n\nStep 2:\n\n\n")
step2()

print("\n\n\nStep 3:\n\n\n")
step3()

print("\n\n\nStep 4:\n\n\n")
step4()

print("\n\n\nStep 5:\n\n\n")
step5()

print("\n\n\nStep 6:\n\n\n")
step6()

print("\n\n\nStep 7:\n\n\n")
step7()

print("\n\n\nStep 8:\n\n\n")
step8()

print("\n\n\nStep 9:\n\n\n")
step9()