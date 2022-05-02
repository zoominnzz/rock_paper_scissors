import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

class Player:
    def __init__(self):
        self.num_wins = 0
        self.hand = ''

    def play(self):
        rand_num = random.randint(1, 3)
        if rand_num == 1:
            self.hand = ROCK
            # self.hand = 'rock'
        elif rand_num == 2:
            self.hand = PAPER
            # self.hand = 'paper'
        else:
            self.hand = SCISSORS
            # self.hand = 'scissors'

    def feedback(self, opponent):
        if self.hand == opponent.hand:
            return 'draw'

        if self.hand == ROCK:
            if opponent.hand == PAPER:
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'

        elif self.hand == PAPER:
            if opponent.hand == SCISSORS:
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'

        else:
            if opponent.hand == ROCK:
                return 'lose'
            else:
                self.num_wins += 1
                return 'win'