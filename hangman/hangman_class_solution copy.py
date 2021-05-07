'''Terminal version of hangman'''
from stages import stages
import random
import os


class Hangman:
    def __init__(self):
        # following 3 lines read the words file, strips away new lines and turns it to a list
        # and then randomly chooses a word from that list
        self._f = open("words.txt", "r")
        self._words = words = [ x.rstrip() for x in f]
        self._choosen_word = random.choice(words)
        # comment in the next line for testing or if you are a cheater
        # print(f"Psst, the word is {choosen_word}")
        self._lives = 6
        self._guesses = []
        print('Welcome to Hangman!')

    def display_game(self):

        display = [ "_" for x in range(len(self._choosen_word))]
        print(' '.join(display))
        print(stages[self._lives])


    def check_guess(self):


    
   

    play = True
    while play:
        guess = input("Guess a letter: ").lower()
        os.system('clear')
        
        if guess in display or guess in guesses:
            print(f"You already guessed {guess}, try again, no penalty")
            print(' '.join(display))
            print(stages[lives])
            continue

        guesses.append(guess)

        for count, letter in enumerate(choosen_word):
            if letter == guess:
                display[count] = letter

        if guess not in choosen_word:
            lives -= 1
            print(f"Sorry, {guess} is not in the word...")
            if lives == 0:
                play = False
                print(f"YOU LOSE! The word was {choosen_word}.")    

        print(' '.join(display))
        print(stages[lives])
        print(f"You have guessed: {guesses}")

        if "_" not in display:
            play = False
            print(f"{choosen_word} was the word! YOU WIN!")

hangman()