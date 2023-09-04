class DevCardDeck:

    def __init__(self):
        pass

class DevCard:
    def __init__(self, owner):
        pass

    def play(self):
        pass

class RoadBuilding(DevCard):
    name = 'road building'

    def play(self):
        # Owner plays two roads

class Monopoly(DevCard):
    name = 'monopoly'

class YearOfPlenty(DevCard):
    name = 'year of plenty'

class VictoryPoint(DevCard):
    name = 'victory point'

class Knight(DevCard):
    name = 'knight'