import random 

MIN_NUMBER = 0
MAX_NUMBER = 100

def main():
    
    num_guesses = 0
    lower_limit = MIN_NUMBER
    upper_limit = MAX_NUMBER

    while True:
        num_guesses += 1
        guess = random.randint(lower_limit, upper_limit)

        user_response = input("Is your number " + str(guess) + "?")
        
        if user_response == 'higher':
            lower_limit = guess + 1
        if user_response == 'lower':
            upper_limit = guess - 1
        if user_response == 'correct':
            break

    print("I win! It took me " + str(num_guesses) + " guesses")

if __name__ == "__main__":
    main()