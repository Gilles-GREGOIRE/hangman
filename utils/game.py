import random
# CLass creation
class Hangman:
        # Attributs creation
    def __init__(self) -> None:
        self.possible_words: list[str] = ["becode", "learning", "mathematics", "sessions", "football", "tennis", "running", "table", "chair", "problem", "understandable", "book"]
        self.word_to_find: list[str] = list(letter for letter in random.choice(self.possible_words))
        self.lives: int = 5
        self.correctly_guessed_letters: list[str] = list("_" for letter in self.word_to_find)
        self.wrongly_guessed_letters: list[None] = []
        self.turn_count: int = 0
        self.error_count : int = 0
        self.already_proposed_letter: list[None] = []

    def __str__(self) -> str:
        return f"{self.correctly_guessed_letters}, {self.wrongly_guessed_letters}, {self.lives}, {self.error_count}, {self.turn_count}"
    
    # Methods creation
    def play(self):
        print(self.correctly_guessed_letters)
        while True:
            self.input_letter = input('Entrez votre lettre :')
            self.input_letter = self.input_letter.lower()
            if self.input_letter.isalpha() and len(self.input_letter) == 1:
                if self.input_letter in self.already_proposed_letter:
                    print ("You already have chosen this lettre, please try with another one")
                else:
                    if self.input_letter in self.word_to_find:
                        for index, letter in enumerate(self.word_to_find):
                            if letter == self.input_letter:
                                self.correctly_guessed_letters[index] = self.input_letter
                                self.already_proposed_letter.append(self.input_letter)
                    else:
                        self.wrongly_guessed_letters.append(self.input_letter)
                        self.already_proposed_letter.append(self.input_letter)
                        self.error_count += 1
                        self.lives -= 1
                    self.turn_count += 1
                    print(self)
                    if self.correctly_guessed_letters == self.word_to_find:
                        break
                    if self.lives == 0:
                        break     
            else:
                print("please, enter a single LETTER")

    def start_game(self):
            self.play()
            if self.lives == 0:
                self.game_over()
            else:
                self.well_played()
        
    def game_over(self):
            print("game over ...")

    def well_played(self):
            print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors !")