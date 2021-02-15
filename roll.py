#This program will simulate the rolling of d3, d4, d6, d8, d10, d12, d20, and d100 dice.

import random
import sys

def menu():
    print('Welcome to Roll!')
    print('Enter the number of sides the dice you wish to roll has. For example, if you wish to roll a d6 enter 6.')
    print('Press q to quit.')
    sides = input('>')
    if sides == '3':
        d3()
    elif sides == '4':
        d4()
    elif sides == '6':
        d6()
    elif sides == '8':
        d8()
    elif sides == '10':
        d10()
    elif sides == '12':
        d12()
    elif sides == '20':
        d20()
    elif sides == '100':
        d100()
    elif sides == 'q':
        sys.exit('Bye!')
    else:
        print('Not a valid option!')
        menu()

def d3():
    x = input('Roll a d3? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 3)
        print(roll)
        d3()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d3()

def d4():
    x = input('Roll a d4? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 4)
        print(roll)
        d4()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d4()

def d6():
    x = input('Roll a d6? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 6)
        print(roll)
        d6()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d6()

def d8():
    x = input('Roll a d8? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 8)
        print(roll)
        d8()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d8()

def d10():
    x = input('Roll a d10? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 10)
        print(roll)
        d10()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d10()

def d12():
    x = input('Roll a d12? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 12)
        print(roll)
        d12()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d12()

def d20():
    x = input('Roll a d20? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 20)
        print(roll)
        d20()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d20()

def d100():
    x = input('Roll a d100? Y/N: ').lower()
    if x == 'y':
        roll = random.randint(1, 100)
        print(roll)
        d100()
    elif x == 'n':
        menu()
    else:
        print('That is not a valid option!')
        d100()

menu()