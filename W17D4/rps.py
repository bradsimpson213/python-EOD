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

    @property
    def player(self):
        return self._player_choice

    @player.setter
    def player(self):
        play = True
        while play:
            player_input = str(input('Choose your move ( rock, paper, or scissors): '))
            if player_input in self._choices:
                self._player_choice = player_input
            else:
                print(f'"{player_input}" is not a valid move, please try again')

    @property
    def computer(self):
        return self._computer_choice

    @computer.setter
    def computer(self):
        self._computer_choice = random.choice(self._choices)

    def report_score(self):
        '''Returns the game score'''
        print(f'''Current score is {self._score['wins']} Wins, {self._score['ties']} Ties, 
            and {self._score['losses']} Losses...''')
        play_again = input("Would you like to play again (yes or no)?: ")
        if play_again == 'yes':
            os.system('\clear')
            return True
        else:
            print(f"{self.player}'s final score was {self.wins} Wins, {self.ties} Ties, and {self.losses} Losses")
            return False

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


play_rps = RockPaperScissors()
while play_rps.report_score():
    play_rps.player()
    play_rps.computer()
    play_rps.decide_winner()
    play_rps.report_score()
# help(RockPaperScissors)
   
            

