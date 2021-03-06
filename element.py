class Element:
    def __init__(self):
        pass
    def damageDealt(self, mob):
        finalDamage = self.basicDamage - mob.armor
        if finalDamage <= 0:
            finalDamage = 0
        mob.hp -= finalDamage

class Empty():
    def __init__(self):
        self.basicDamage = 0
        self.index = 0
        self.price = 0
        self.attackSpeed = 0
        self.attackRange = 0


class Fire(Element):
    def __init__(self):
        self.basicDamage = 20
        self.index = 11
        self.price = 1
        self.attackSpeed = 300
        self.attackCounter = self.attackSpeed
        self.attackRange = 100
        self.splashRange = 50
        self.splashDamage = 1
        self.attackColor = (255,0,0)
        self.image = "ElementIcon/fire.png"


class Water(Element):
    def __init__(self):
        self.basicDamage = 15
        self.index = 21
        self.price = 1
        self.attackSpeed = 800
        self.attackCounter = self.attackSpeed
        self.attackRange = 200
        self.slowPercentage = 0.4
        self.attackColor = (0,0,255)
        self.image = "ElementIcon/drop.png"

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
