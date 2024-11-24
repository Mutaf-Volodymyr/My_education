from random import randint

# table
# ball
# bets
# players


from random import randint






class Game:
    def __init__(self, player: object, table: object):
        self.player = player
        self.table = table
        self.winner = None
        self.numers_bet = []

    def accept_the_bet(self):
        while True:
        self.numers_bet.append(self.player.make_bet())

class Player:
    def __init__(self, name: str, cash: float):
        self.name = name
        self.cash = cash

    def make_bet(self):
        bet = float(input("Make a bett:"))
        number = int(input("Choose the number:"))
        return bet, number



class Table:
    def __init__(self, ):
        self.win_number = None

    def spin_the_wheel(self):
        self.win_number = randint(0, 36)




elena = Player('Elena', 1000)
table1 = Table()
game = Game(elena, table1)











