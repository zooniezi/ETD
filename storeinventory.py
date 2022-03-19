import element
import Gold
import random

availableElements = [11,21]
gold=Gold.Gold()
##################################################################################
#확인용 변수들
roundNumber=1

##################################################################################

class Store:
    def __init__(self):
        self.rerollCost=2                                                  
        self.shelf = [0, 0, 0]
        for i in range(3):
            self.shelf[i] = elementGenerate(random.sample(availableElements, 1))

    def reroll(self):
        gold.playerGold -= self.rerollCost
        for i in range(3):
            self.shelf[i] = elementGenerate(random.sample(availableElements, 1))
        
    def buy(self, element):
        gold.playerGold -= element.price
        #self.shelf[shelfNumber]]=0 #산 원소가 있었던 칸 비우기
        elementGenerate(element.index)   
                                                                                    #고정되어있는 원소 백과사전를 참조해서 인generate매소드를 사용해서 인벤토리에 새로운 원소 class를 생성해야함
                                                                                    #그리고 그 원소의 가격에 elt.price = real_price 대입해줘야 나중에 팔때 산가격에 팔수 있음->generate_element에서 해줘야할일
        
    def sell(self, eltInInventory):
        gold.playerGold += (eltInInventory.price)/2                                 #밸런싱 필요
        del eltInInventory

##################################################################################

class InventoryAndFactory:
    def __init__(self):
        self.inventory=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.factory=[0, 0, 0]                                                        #조합버튼이 따로 있음

    def addFactory(self, inventoryNum, factoryNum):
        self.factory[factoryNum]=self.inventory[inventoryNum]
        self.inventory[inventoryNum]=0

    def addInventory(self, inventoryNum, factoryNum):
        self.inventory[inventoryNum]=self.factory[factoryNum]
        self.factory[factoryNum]=0
    
    #if 조합버튼을 누르면
    def compoundMix(self):
        pass                                                                        #나중에 추가
    
    def compoundLevelUp(self):
        self.factory=[0, 0, 0]
        self.factory[0]=self.elementGenerate()
        for i in range(9):
            if self.inventory[i]==0:
                self.addInventory[i,0]

def elementGenerate(indexOfElement):
    #index of fire is assumed by 11
    if indexOfElement==11:
        return element.Fire()
    #index of fireLevel2 is assumed by 12
    if indexOfElement == 12:
        return element.FireLevel2()
    #index of water is assumed by 21
    if indexOfElement == 21:
        return element.Water()
    #index of waterLevel2 is assumed by 22
    if indexOfElement == 22:
        return element.WaterLevel2()

def findIndexMix():
    pass
#if indexNum1==indexNum2 and indexNum2==indexNum3:
def findIndexLevelUp(indexNum):
    return indexNum+1
    
def addTower(inventoryNum, towerNum, towermaster):
    towermaster[towerNum].element=inventoryAndFactory.inventory[inventoryNum]
    inventoryAndFactory.inventory[inventoryNum]=0
##################################################################################

inventoryAndFactory=InventoryAndFactory()
store=Store()

##################################################################################
#확인용 출력부
store.buy(A)                                                                        #어떻게 원소를 넣을지 나중에 생각해야함
print(gold.playerGold)
store.sell(A)
print(gold.playerGold)
store.sell(B)
print(gold.playerGold)
store.reroll()
print(gold.playerGold)
store.reroll()
print(gold.playerGold)
print(store.shelf)