class hangman:
    def __init__(self, word):
        self.word = word
        self.chances = len(word) + 4

    def __str__(self):
        return f'You have {self.chances} chances'
    
    def guess(self,guess):
        for letter in self.word:
            if guess in self.word:
                self.word = self.word.replace(letter, "")
                self.chances = self.chances - 1
                return True
            else:
                self.chances = self.chances - 1
                return False
    def empty(self):
        if len(self.word) <= 1:
            return False
        else:
            return True
    def chance(self):
        if self.chances <= 1:
            return False
        else:
            return True