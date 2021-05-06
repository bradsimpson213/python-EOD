import random
import os

class RockPaperScissors:
    '''Class to create games of Rock Paper Scissors'''
    def __init__(self, player="player 1"):
        self._player1 = input("Please enter your player name: ")
        self._choices = ('rock', 'paper', 'scissors')
        self._player = ''
        self._computer = ''
        self._score = {'wins': 0, 'losses': 0, 'ties': 0}

    def report_score(self):
        '''Returns the game score'''
        print(f"Current score is {self._score['wins']} Wins, {self._score['ties']} Ties, and {self._score['losses']} Losses...")
        play_again = input("Would you like to play again (yes or no)?: ")
        if play_again == 'yes':
            os.system('\clear')
            self.player_move()
        else:
            print(f"{self._player1}'s final score was {self._score['wins']} Wins, {self._score['ties']} Ties, and {self._score['losses']} Losses")


    def decide_winner(self):
        '''Determines the results of a game round (win/loss/tie)'''
        if self._player == self._computer:
            print(f'{self._player1} and the Computer both chose "{self._player}", its a Tie!')
            self._score['ties'] += 1 
        elif ((self._player == 'rock' and self._computer == 'scissors')
            or (self._player == 'paper' and self._computer == 'rock')
            or (self._player == 'scissors' and self._computer == 'paper')):
            print(f'{self._player1} played "{self._player}" and the Computer played "{self._computer}", You Win!')
            self._score['wins'] += 1
        else:
            print(f'{self._player1} played "{self._player}" and the Computer played "{self._computer}", You Lose!')
            self._score['losses'] += 1
        self.report_score()


    def computer_move(self):
        '''Generated a random computer game move'''
        self._computer = random.choice(self._choices)
        self.decide_winner()


    def player_move(self):
        '''Prompts game player for move input'''
        play = True
        while play:
            player_input = input('Choose your move ( rock, paper, or scissors): ')
            if player_input in self._choices:
                self._player = player_input
                play = False
            else:
                print(f'"{player_input}" is not a valid move, please try again')
        self.computer_move()


play_game = RockPaperScissors()
play_game.player_move()
