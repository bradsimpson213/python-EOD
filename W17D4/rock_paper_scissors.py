import random

class RockPaperScissors:
    def __init__(self, player="player 1"):
        self.player = player
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.choices = [ 'rock', 'paper', 'scissors']
        self.player_choice = ''
        self.computer_choice = ''

    def decide_winner(self):
        if self.player_choice == self.computer_choice:
            print(f'{self.player} and the Computer both chose {self.player_choice}, its a Tie!')
            return
        if ((self.player_choice == 'rock' and self.computer_choice == 'scissors')
             or (self.player_choice == 'paper' and self.computer_choice == 'rock')
             or (self.player_choice == 'scissors' and self.computer_choice == 'paper')):
            print(f'{self.player} played "{self.player_choice}" and the Computer played "{self.computer_choice}", You Win!')
        else:
            print(f'{self.player} played "{self.player_choice}" and the Computer played "{self.computer_choice}", You Lose!')

    def computer_move(self):
        self.computer_choice = random.choice(self.choices)
        self.decide_winner()

    def player_move(self):
        play = True
        while play:
            player_input = input('Choose your move ( rock, paper, or scissors): ')
            if player_input in self.choices:
                self.player_choice = player_input
                play = False
            else:
                print(f'"{player_input}" is not a valid move, please try again')
        self.computer_move()
        



play_game = RockPaperScissors('Brad')
play_game.player_move()
   
            

