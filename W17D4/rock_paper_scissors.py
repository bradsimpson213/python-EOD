import random

class RockPaperScissors:
    def __init__(self, player="player 1" )
        self.player = player
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.choices = [ 'rock', 'paper', 'scissors']
        self.player_choice = ''
        self.computer_choice = ''

    
    def computer_move (self):
        self.computer_choice = random.choices(self.choices)

    def player_move (self):
        play = True
        while play:
            player_input = input('Choose your move ( rock, paper, or scissors): ')
            if player_input in self.choices:
                self.player_choice = player_input
                play = False
            else:
                print(f'{player_input} is not a valid move, please try again')
        self.computer_move()
        

   
            

