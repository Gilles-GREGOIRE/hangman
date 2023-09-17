# Hangman game
the hangman game is a classic word-guessing game where the player attempts to guess a hidden word one letter at a time, with limited incorrect guesses allowed.

## How to play

1. **Installation**
   - Ensure you have Python installed on your system.
   - Clone this repository or download the `hangman` repository.

2. **Running the Game**
   - Open a terminal/command prompt and navigate to the directory (hangman) where `main.py` is located.
   - Run the game by typing the following command:
     ```
     python main.py
     ```

3. **Usage**
   - The game selects a random word from a predefined list.
   - Enter a letters each round.
   - You begin with 5 lives The game selects a random word from a predefined list.
   - For each wrong letter as imput, you loose 1 life.
   - For each letter in the word as input, the program will display the letters at their own position in the word. The player conserve his lives (5 at start).
   - the player looses if he doesn't find all the letters before he has nomore lives (5 wrong letters).
   - The player wins if he finds all the letters before he has nomore lives.
   - After each round, player will be informed of his results.

4. **Contributors**
   - Alexandre Bove
   - Louise De Rous
   