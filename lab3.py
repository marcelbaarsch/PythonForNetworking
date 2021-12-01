#!/usr/bin/env python3
# Lab 3 - Loops, Conditional execution, logical and bitwise operations
# Marcel Baarsch - marcelbaarsch@gmail.com

#
# Steps are seperated out functions.
#

import math
# import pdb # python debugger

def step1():
    name1 = input("Enter First name: ") # 1. Ask the user for a Name:
    name2 = input("Enter Second name: ") # 2. Ask for another name:

    print ("Here are your names in alphabetical order.") # 3. output
    
    # 4. Conditional when name1 lower then name 2
    if name1 < name2: # 5. TRUE
        print (name1 + "\n" + name2)
    else: # 6. FALSE
        print (name2 + "\n" + name1)

def step2():
    age = int(input("What is the customer's age: ")) # 1. Ask for customer's age
    
    # 2. conditional on age
    if age <= 2:
        price = 0.00
    elif age <= 13:
        price = 7.99
    elif age >= 65:
        price = 9.99
    elif age <= 64:
        price = 12.99
    
    # 3.
    if price == 0:
        print ("You're too young to purchase.")
    else:
        print (f'If the customer is {age} the tickets cost ${price}')

def step3(): # Challenge
    # Write a program to ask the user for a number.
    number = float(input ("Please enter a number: "))
    roundedNumber = round(number) # If a fraction is entered, round to nearest whole number

    # print out if number is...
    if roundedNumber > 0: # Positive
        print(f'Your number {roundedNumber} is a positive number')
    elif roundedNumber < 0: # Negative
        print(f'Your number {roundedNumber} is a negative number')
    else: # or zero
        print(f'Your number is a zero')

def step4():
    start_num = 0 
    while start_num <= 0:

        # 1. Ask for a starting number, 2. round to nearest whole number if fraction is entered
        start_num = round(float(input("Please Enter a Starting number: ")))
        
        if start_num > 0: # 4. if start_num is larger than zero
            print (f'Counting down from {start_num} to zero.')
            for i in range(start_num, 0, -1):
                print (f'{i} , ',end='')
            print('0.')
            break

        else: # 3. If start_num is zero or negative
            print ("Please enter a positive number.")

def step5():
    # 1. Ask for a word
    word = input("Please Enter a Word: ")

    count = 0

    # 2. Loop [char] for each letter in the word
    for char in word:
        # 2. a. If [char] = vowel increment [count]
        if char in 'aeiouyAEIOUY':
            count +=1

    # 3. output
    print (f'There are {count} vowels in the word "{word}"')

def step6(): # Challenge
    # Write a program that adds up the items purchased at a store
    # Then calculate the total of all items and the average price of the items entered.
    #
    # Ask the user for the price of an item
    # Stop the loop when the user enters -1
    # DO NOT ADD -1 to your total or count
    #
    # After adding an [item] increment the [count] of items and the [item] price to a [total].

    print ("Enter -1 to Finish Your List.")

    price = 0
    total_items = 0

    while True:
        p = float(input("Please enter the items price: "))
        if p == -1:
            break
        else:
            price += p
            total_items += 1
        
    print(f'You entered {total_items} items for a total bill of ${price}.')
    print('Your average item price was $' + str(price/total_items))
            
# Convert Decimal to Binary
def step7():
    # DO NOT USE bin() FUNCTION. Use division by two method

    # 1. Ask user for a Decimal. Store the answer in a variable [dec]. Make sure the input is an INT
    dec = int(input ("Please enter a Decimal value: "))

    # 2. Setup a variable [result] to be a zero length string.
    result = ''

    # 3. Copy the value of [dec] into a variable [num].
    num = dec

    # 4. Loop until the [num] variable is zero
    while num > 0:
        remainder = num%2
        num = math.floor(num / 2)
        result = str(remainder) + result

    # 5. Output
    print(f'The binary representation of {dec} is {result}')

# Convert Binary to Decimal
def step8():
    # DO NOT USE bin()

    # 1. Ask user for a Binary number. Store the answer in a variable [binary]. The input will be str.

    binary = input ("Please enter a Binary value: ")

    # 2. Setup a variable [result] and initialize it to a zero (INT).

    result = 0

    # 3. Setup a variable [count] and set it to be the number of characters (bits) in the [binary] input.
    count = len(binary) - 1

    # 4. Loop through each bit in binary input string
    for bit in binary:
        # pdb.set_trace()
        # a. mathhhhhh
        result += int(bit) * 2**count
        # b. Derement the [count] variable by 1
        count -= 1

    # 5. output
    print(f'The Decimal representation of {binary} is {result}.')

def step9(): # The final challenge??
    # Your mission...Create a program that asks the user for a range (Start to End). You want to output all the 
    # numbers in the range. With each number you will state if the number is even or odd and if the number is 
    # divisible by 3 and / or 4.

    # Program Requirements 
    # 1. Ask User for a Start and End Value.  
    # 2. Make sure both numbers are Integers. 
    # 3. Make sure the end value is bigger than the start number.  
    # 4. Loop through the range from Start to End. 
    # 5. Display the Number followed by the words "is EVEN" or "is ODD" then optionally the words 
    # "and is divisible by 3" or "and is divisible by 4" or "and is divisible by 3 and by 4".

    while True:
        first_number = int(input("Please enter the First Number in the Range: "))
        last_number = int(input("Please enter the Last Number in the Range: "))
    
        if first_number < last_number:
            for x in range(first_number, last_number+1, 1):
                
                if x % 2 == 0:
                    print (f'{x} is even',end='')
                    if x % 3 == 0 and x % 4 == 0:
                        print (" and is divisble by 3 and by 4.")
                    elif x % 3 == 0:
                        print (" and is divisble by 3.")
                    elif x % 4 == 0:
                        print (" and is divisble by 4.")
                    else:
                        print (".")
                
                else:
                    print (f'{x} is odd',end='')
                    if x % 3 == 0:
                        print (" and is divisble by 3.")
                    else:
                        print (".")
                    
            break



# RUN ALL THE STEPS! Comment them out if you only want to run one at a time

print ("STEP 1: \n\n\n")
step1()

print ("\n\n\nSTEP 2: \n\n\n")
step2()

print ("\n\n\nSTEP 3: \n\n\n")
step3()

print ("\n\n\nSTEP 4: \n\n\n")
step4()

print ("\n\n\nSTEP 5: \n\n\n")
step5()

print ("\n\n\nSTEP 6: \n\n\n")
step6()

print ("\n\n\nSTEP 7: \n\n\n")
step7()

print ("\n\n\nSTEP 8: \n\n\n")
step8()

print ("\n\n\nSTEP 9: \n\n\n")
step9()
