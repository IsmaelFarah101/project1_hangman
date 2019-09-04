##this is the class that creates the hangman game
class hangman:
    def __init__(self, word):
        ##this is where we initialize the instance variables
        self.word = word
        self.chances = len(word) + 4
        ## this returns the chances left
    def __str__(self):
        return f'You have {self.chances} chances'
    ##this allows the user to guess the word if the user guesses correctly it returns true and deletes the letter or letters from the word
    # if the user guesses wrongly it returns false 
    def guess(self,guess):
        for letter in self.word:
            if guess in self.word:
                self.word = self.word.replace(letter, "")
                self.chances = self.chances - 1
                return True
            else:
                self.chances = self.chances - 1
                return False
    ##this returns the boolean of the amount of letters left in the word
    def empty(self):
        if len(self.word) <= 1:
            return False
        else:
            return True
    ##this returns the boolean of the amount of chances left
    def chance(self):
        if self.chances <= 1:
            return False
        else:
            return True