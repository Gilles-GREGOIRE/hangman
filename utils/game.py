# Exercice 1 : Hangman
import random # import of the random library to enable radom.choice() Method use

# Hangman class creation
class Hangman:

    def __init__(self) -> None: # creation of the init method to define class attibutes
        self.possible_words: list[str] = ["becode", "learning", "mathematics", "sessions", "football", "tennis", "running", "table", "chair", "problem", "understandable", "book"] # list of possible word to guess
        self.word_to_find: list[str] = list(letter for letter in random.choice(self.possible_words)) # use of the random.choice method to select a word in the list
        self.lives: int = 5 # initialize the number of lives at 5 (start)
        self.correctly_guessed_letters: list[str] = list("_" for letter in self.word_to_find) # initialization of the word to find in termes of _ characters
        self.wrongly_guessed_letters: list[None] = [] # initialize un empty list
        self.turn_count: int = 0 # intialize the turn counter to 0 (start)
        self.error_count : int = 0 # initialize the error counter to 0 (start)
        self.already_proposed_letter: list[None] = [] # initialize un empty list that will countain the already proposed letter

    def __str__(self) -> str: # creation of the str method to return all the parameters to inform the player of the current situation after each round
        return f"{self.correctly_guessed_letters}, {self.wrongly_guessed_letters}, {self.lives}, {self.error_count}, {self.turn_count}"
    
    def play(self): # creation of the play method
        print(self.correctly_guessed_letters) # display the initial length of the word to find
        while True: # initialization of an infinite while loop to perfom round after round
            self.input_letter = input('Entrez votre lettre :') 
            self.input_letter = self.input_letter.lower() # put the input letter in a lower case to fit the letters in the word to find
            if self.input_letter.isalpha() and len(self.input_letter) == 1: # condition to ensure that the player will input only one letter
                if self.input_letter in self.already_proposed_letter: # condition to ensure that the player will not be able to input the same letter 2 times
                    print ("You already have chosen this lettre, please try with another one")
                else: # treatment of the input letter
                    if self.input_letter in self.word_to_find: # test to define if the letter is in the word and the treatment if the letter is inside
                        for index, letter in enumerate(self.word_to_find): # get the index of each letter 
                            if letter == self.input_letter: # display the letter at the correct index
                                self.correctly_guessed_letters[index] = self.input_letter
                                self.already_proposed_letter.append(self.input_letter) # add the letter to the list of already proposed letters
                    else: # treatment if de letter is not in the word
                        self.wrongly_guessed_letters.append(self.input_letter) # add the letter to the list of wrongly guessed letters
                        self.already_proposed_letter.append(self.input_letter) # add the letter to the list of already proposed letters
                        self.error_count += 1 # add 1 to the error counter
                        self.lives -= 1 # remove a life
                    self.turn_count += 1 #add 1 to the turn counter
                    print(self) # dispay str method with all informations after each round
                    if self.correctly_guessed_letters == self.word_to_find: # going out of the loop when all the letters are found
                        break
                    if self.lives == 0: # going out of the loop when the lives reach 0
                        break     
            else:
                print("please, enter a single LETTER") # display un error message if the player try to enter the same letter 2 times

    def start_game(self): # method start game defintion to start the game and initialize play method
            self.play()
            if self.lives == 0: # initialize the game over method when the is no more lives
                self.game_over()
            else: # initialize the well played method when the player has guessed all the letters
                self.well_played()
        
    def game_over(self): # method to display game over 
            print("game over ...")

    def well_played(self): # method to display the winning informations
            print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors !")