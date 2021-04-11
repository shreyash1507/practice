from random import randint
import math


name = input("Enter your name: ")
print(f'\nHello, {name}')
print('Welcome to number guessing game\n')

tries = 9

def hints(tries, num):
    if tries == 8:
        if num % 2 == 0:
            print('Number is even')
        else:
            print('Number is odd')

    if tries == 6:
        print(f'Number is greater than {math.ceil(num/2)}')
    
    if tries == 4:
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19,
                        23, 29, 31, 37, 41, 43,
                        47, 53, 59, 61, 67, 71, 
                        73, 79, 83, 89, 97]
        if num in prime_list:
            print('Number is Prime')
        else:
            factors = [x for x in range(1,num+1) if num%x ==0]
            print(f'Number is divisible by {factors[-2]}')

    if tries == 2:
        upper = (math.floor(num/10)+1)*10
        lower= upper - 10
        print(f'Number lies between {lower} and {upper}')
    

def gameplay():
    global tries
    randnum = randint(1,101)
    print('Random number generated between 1 and 100\n')

    while True:
        print(f'\nTries: {tries}')
        hints(tries, randnum)
        try:
            guess = int(input('Take a guess: '))
        except ValueError:
            print('Please enter an integer value')
            continue
        else:
            if guess == randnum:
                print('\nCongratulations! You Win!')
                break
            elif tries == 1:
                print('\nYou Lose')
                print(f'The number was: {randnum}')
                break 
            else:
                print('\nOOPS! Wrong guess.\n')
                tries = tries-1
                continue
        
    
    replay=  input('\nWant to play again? y/n ')
    if replay == 'y':
       
        gameplay()
    else:
        exit
        
gameplay()