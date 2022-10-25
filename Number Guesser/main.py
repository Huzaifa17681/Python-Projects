import random
import os
import time

value1  = input("\n1 Easy \n2 Medium \n3 Hard \nSelect Difficulty, Enter Number: ")

#Make sure if input is a digit
try:
    int(value1)
    val = True 
except ValueError:
    print('Please enter a digit!')
difficulty = int(value1)
#Main Work
if difficulty == 1:
    n = random.randrange(1,5)
    x = input('Please enter a number (1 - 5): ')
    try:
        int(x)
        val = True 
    except ValueError:
        x = int(input('Please enter a digit: '))
    x = int(x)
    while x != n:
        if x > n:
            print("High\n")
            x = int(input('Enter the number again: '))
        elif x < n:
            print("Low\n")
            x = int(input('Enter the number again: '))
        elif x == n:
            break
    print("You guessed the number right")
elif difficulty == 2:
    n = random.randrange(1,10)
    x = input('Please enter a number (1 - 10): ')
    try:
        int(x)
        val = True 
    except ValueError:
        x = int(input('Please enter a digit: '))
    x = int(x)
    while x != n:
        if x > n:
            print("High\n")
            x = int(input('Enter the number again: '))
        elif x < n:
            print("Low\n")
            x = int(input('Enter the number again: '))
        elif x == n:
            break
    print("You guessed the number right")
elif difficulty == 3:
    n = random.randrange(1,20)
    x = input('Please enter a number (1 - 20): ')
    try:
        int(x)
        val = True 
    except ValueError:
        x = int(input('Please enter a digit: '))
    x = int(x)
    while x != n:
        x = int(input("Enter the value again: "))
        if x == n:
            break
    print("You guessed the number right")
else:
    print('Error')

time.sleep(1)
os.system('cls')
#again option comin soon

#coded by huzaifa
