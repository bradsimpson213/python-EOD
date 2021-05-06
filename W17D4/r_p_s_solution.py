import random
import os

class RockPaperScissors:
    '''Class to create games of Rock Paper Scissors'''
    def __init__(self, player="player 1"):
        self._player = input("Please enter your player name: ")
        self._choices = ('rock', 'paper', 'scissors')
        self._player_choice = None
        self._computer_choice = None
        self._score = {'wins': 0, 'losses': 0, 'ties': 0}
        self.player = input('Choose your move ( rock, paper, or scissors): ')

    @property
    def player(self):
        return self._player_choice

    @player.setter
    def player(self, value):
        if value in self._choices:
            self._player_choice = value
            self.computer = random.choice(self._choices)
        else:
            print(f'"{value}" is not a valid move, please try again')
            self.player = input('Choose your move ( rock, paper, or scissors): ')

    @property
    def computer(self):
        return self._computer_choice

    @computer.setter
    def computer(self, value):
        self._computer_choice = value
        self.decide_winner()

    def decide_winner(self):
        '''Determines the results of a game round (win/loss/tie)'''
        if self.player == self.computer:
            print(f'{self._player} and the Computer both chose "{self.player}", its a Tie!')
            self._score['ties'] += 1 
        elif ((self.player == 'rock' and self.computer == 'scissors')
            or (self.player == 'paper' and self.computer == 'rock')
            or (self.player == 'scissors' and self.computer == 'paper')):
            print(f'{self._player} played "{self.player}" and the Computer played "{self.computer}", You Win!')
            self._score['wins'] += 1
        else:
            print(f'{self._player} played "{self.player}" and the Computer played "{self.computer}", You Lose!')
            self._score['losses'] += 1
        self.report_score()

    def report_score(self):
        '''Returns the game score'''
        print(f'''Current score is: 
            {self._score['wins']} Wins {self._score['ties']} Ties {self._score['losses']} Losses''') 
        play_again = input("Would you like to play again (yes or no)?: ")
        if play_again == 'yes':
            os.system('\clear')
            self.player = input('Choose your move ( rock, paper, or scissors): ')
        else:
            print(f'''{self._player}'s final score was: 
                {self._score['wins']} Wins {self._score['ties']} Ties {self._score['losses']} Losses''')
            

play_rps = RockPaperScissors()


   # def player_move(self):
    #     '''Prompts game player for move input'''
    #     self.player = input('Choose your move ( rock, paper, or scissors): ')
   
    # def computer_move(self):
    #     '''Generated a random computer game move'''
    #     self.computer = random.choice(self._choices)