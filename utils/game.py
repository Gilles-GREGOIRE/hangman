import random
# CLass creation
class Hangman:
        # Attributs creation
    def __init__(self) -> None:
        self.possible_words = ["becode", "learning", "mathematics", "sessions", "football", "tennis", "running", "table", "chair", "problem", "understandable", "book"]
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = list("_ " for letter in self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0    
    
    # Methods creation
    def play (self):
        self.input_letter = input('Entrez votre lettre :')
        if self.input_letter == self.input_letter.isalpha() and len(1):
            if self.input_letter in self.word_to_find:
                for self.input_letter, index in enumerate(self.word_to_find):
                    self.correctly_guessed_letters[index] = self.input_letter

        else:
                
        #if type(self.input_letter) != str:


    #def start_game ():
    #def game_over ():
    #def well_played ():

Hangman()