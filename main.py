##importing the nessacaty modules
import random
from hangman import hangman
##opening a file of random words for the user to guess
wordFile = open('words.txt').read().splitlines()
##getting the word
word = random.choice(wordFile)
##initiating the game
game = hangman(word)
##I printed the word just to check if the logic worked 
print(word)
guess = input('Enter a single character in the word: ')
while guess:
    ##checks if the user has any chances left
    if game.chance():
        ##checks if the user successfully guesed the word
        if game.empty():
            ##checks if the user correctly guesses a letter
            if game.guess(guess[0]):
                print('You got one')
                print(game)
                guess = input('Enter a single character in the word: ')
            else:
                print(game)
                print('You lost one')
                guess = input('Enter a single character in the word: ')
        else:
            print('You guessed the word correctly')
            break
    else:
        print('You ran out of chances')
        break