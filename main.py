import random
from hangman import hangman
wordFile = open('words.txt').read().splitlines()
word = random.choice(wordFile)
game = hangman(word)
print(game)
print(word)
guess = input('Enter a single character in the word: ')
while guess:
    if game.chance():
        if game.empty():
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