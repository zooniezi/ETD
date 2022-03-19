class gold:
    def __init__(self):
        self.player_gold=100
    
    def gain_gold(self, plus_gold):
        self.player_gold += plus_gold
    
    def lose_gold(self,minus_gold):
        self.player_gold -= minus_gold
Gold = gold()