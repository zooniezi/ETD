class Element:
    def __init__(self):
        pass
    def damageDealt(self, mob):
        finalDamage = self.basicDamage - mob.armor
        mob.hp -= finalDamage

class Fire(Element):
    def __init__(self, basicDamage, price, attackSpeed, attackRange, splashRange, splashDamage):
        super.__init__()
        self.basicDamage = 10
        self.price = 1
        self.attackSpeed = 1
        self.attackRange = 100
        self.splashRange = 50
        self.splashDamage = 10

class Water(Element):
    def __init__(self, basicDamage, price, attackSpeed, attackRange, slowPercentage):
        super.__init__()
        self.basicDamage = 5
        self.price = 1
        self.attackSpeed = 1
        self.attackRange = 100
        self.slowPercentage = 0.4

    def slow(self, mob):
        mob.speed = mob.speed*(1-self.slowPercentage)