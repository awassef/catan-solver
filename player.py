class Player:

    def __init__(self):
        self.dev_cards = []
        self.resource_cards = []
        self.victory_points = 0
        self.num_settlements = 0
        self.num_cities = 0
    
    def possible_moves(self, board):
        pass

    def _buy(self, resources: list):
        '''
        Attempt to buy with resource list. If player cannot buy, 
        return False. If player can buy, return True.
        '''
        for (resource, num_resource_required) in resources.items():
            if resource not in self.resource_cards:
                return False 
            if self.resource_cards.count(resource) < num_resource_required:
                return False
        return True 

    def buy_dev_card(self):
        self._buy(
            {'ore': 1,
             'grain': 1,
             'wool' : 1}
        )

    def buy_settlement(self):
        self._buy(
            {'ore': 1,
             'grain': 1,
             'wool' : 1}
        )


    def buy_city(self):
        pass

    def buy_road(self):
        pass

    def play_dev_card(self):
        pass