import random
words = []
myfile = open('Lexicon.txt', 'r')
for word in myfile:
    words.append(word)
myfile.close()

valid_inputs= ['A','B','C','D', 'E','F','G',
                    'H','I','J','K','L','M','N',
                    'O','P','Q','R','S','T','U',
                    'V','W','X','Y','Z']
tries = 8;
user_entry = []
entered_letters = []

def word_generate():
    gameword = random.choice(words)
    gameword = gameword[:-1]
    for letter in gameword:
        user_entry.append('-')
    return gameword.upper()
def check_ans(guess, gameword):
    global tries
    gameword = gameword.upper()
    if guess in gameword:
        for i in range(len(gameword)):
            if(gameword[i] == guess ):
                user_entry[i] = guess
        print("That guess is correct.")
        print("The word now looks like this: ",''.join(user_entry))
    else:
        print(f"There are no {guess}'s in the word")
        print("The word now looks like this: ",''.join(user_entry))
        tries = tries -1

def game_end(user_entry,gameword):
    if tries == 0:
        print('Sorry, you lost. The secret word was: ',gameword)
        return False
    elif gameword == ''.join(user_entry):
        print('Congratulations, the word is: ',gameword)
    else:
        return True 

def gameplay():
    global tries
    global user_entry
    global entered_letters
    gameword = word_generate()
    print ('The word now looks like this: '+''.join(user_entry))
    while True:
        print(f"You have {tries} guesses left")
        guess = input('Type a single letter here, then press enter: ').upper()
        if guess not in valid_inputs:
            print("Guess should only be a single character.")
            print("The word now looks like this: "+''.join(user_entry))
            continue
        else:
            entered_letters.append(guess)
            check_ans(guess, gameword)
            if game_end(user_entry,gameword):
                continue
            else:
                break
gameplay()