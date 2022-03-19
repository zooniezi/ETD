class Gold:
    def __init__(self):
        self.playerGold=100
    
    def gain_gold(self, plusGold):
        self.playerGold += plusGold
    
    def lose_gold(self,minusGold):
        self.playerGold -= minusGold
GOLD = Gold()