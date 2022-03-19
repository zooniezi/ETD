class Element:
    def __init__(self):
        pass
    def damageDealt(self, mob):
        finalDamage = self.basicDamage - mob.armor
        mob.hp -= finalDamage

class Fire(Element):
    def __init__(self, basicDamage, index, price, attackSpeed, attackRange, splashRange, splashDamage):
        super.__init__()
        self.basicDamage = 10
        self.index = 11
        self.price = 1
        self.attackSpeed = 1
        self.attackRange = 100
        self.splashRange = 50
        self.splashDamage = 1


class Water(Element):
    def __init__(self, basicDamage, index, price, attackSpeed, attackRange, slowPercentage):
        super.__init__()
        self.basicDamage = 5
        self.index = 21
        self.price = 1
        self.attackSpeed = 1
        self.attackRange = 100
        self.slowPercentage = 0.4

    def slow(self, mob):
        mob.speed = mob.speed*(1-self.slowPercentage)

class FireLevel2(Element):
    def __init__(self, basicDamage, index, price, attackSpeed, attackRange, splashRange, splashDamage):
        super.__init__()
        self.basicDamage = 20
        self.index = 12
        self.price = 3
        self.attackSpeed = 2
        self.attackRange = 150
        self.splashRange = 60
        self.splashDamage = 3

class WaterLevel2(Element):
    def __init__(self, basicDamage, index, price, attackSpeed, attackRange, slowPercentage):
        super.__init__()
        self.basicDamage = 5
        self.index = 22
        self.price = 3
        self.attackSpeed = 2
        self.attackRange = 200
        self.slowPercentage = 0.5

    def slow(self, mob):
        mob.speed = mob.speed*(1-self.slowPercentage)