import random
from constants import Resources
# from dev_card import DevCardDeck


class CatanGame:

    def __init__(self, board=None):
        assert isinstance(board, CatanBoard)
        if board is None:
            self.board = CatanBoard()
        else:
            self.board = board 

class CatanBoard:

    def __init__(self, config=None):
        # Config = Board Hexes & #'s
        rolls = list(range(2,13))

        # Number of hexes per roll 
        n_hexes = [2] * len(rolls)
        n_hexes[0] = 1
        n_hexes[-1] = 1

        resource_allocation = {
            Resources.LUMBER: 4,
            Resources.GRAIN: 4,
            Resources.WOOL:4,
            Resources.BRICK: 3, 
            Resources.ORE: 3,
        }

        resource_list = list(resource_allocation.keys())
        resource_num = list(resource_allocation.values())

        random_numbers = random.sample(rolls, sum(n_hexes), counts=n_hexes)
        random_resources = random.sample(resource_list, sum(resource_num), counts=resource_num)

        self.board = []

        for (number, resource) in zip(random_numbers, random_resources):
            self.board.append(CatanHex(number, resource))

         # 0 represents desert       
        self.board.append(CatanHex(0, Resources.DESERT))
        # self.dev_cards = DevCardDeck()
        self.resource_deck = ResourceDeck()

class CatanHex:

    def __init__(self, dice_roll: int, resource: str):
        '''
        dice_roll: int is one of 0 + 2-12
        resource: str is one of wood, wheat, sheep, brick, ore, desert
        '''
        self.dice_roll = dice_roll
        self.resource = resource

    def __str__(self):
        return f'{self.resource} @ {self.dice_roll}'

class ResourceDeck:

    def __init__(self):
        self.lumber = 19
        self.brick = 19
        self.ore = 19
        self.grain = 19 
        self.wool = 19


class Bank: 

    def __init__(self):
        self.resource_deck = ResourceDeck()

if __name__ == '__main__':
    board = CatanBoard()