import element
import random

availableElements = [11,21]
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
#돈을 지불하고 shelf 리스트를 구매 가능한 원소들 중에서 랜덤추출하여 새롭게 갱신
    def reroll(self, gold):
        gold.playerGold -= self.rerollCost
        for i in range(3):
            self.shelf[i] = elementGenerate(random.sample(availableElements, 1))
#shelf에 있는 원소중 해당 가격만큼 돈을 지불하고 
    def buy(self, gold, element, inventoryAndFactory):
        gold.playerGold -= element.price
        #self.shelf[shelfNumber]]=0 #산 원소가 있었던 칸 비우기
        inventoryAndFactory.inventory[inventoryAndFactory.findEmptyIndex()] = elementGenerate(element.index)
         
                                                                                    #고정되어있는 원소 백과사전를 참조해서 인generate매소드를 사용해서 인벤토리에 새로운 원소 class를 생성해야함
                                                                                    #그리고 그 원소의 가격에 elt.price = real_price 대입해줘야 나중에 팔때 산가격에 팔수 있음->generate_element에서 해줘야할일
        
    def sell(self, gold, eltInInventory):
        gold.playerGold += (eltInInventory.price)/2                                 #밸런싱 필요
        del eltInInventory

##################################################################################

class InventoryAndFactory:
    def __init__(self):
        self.inventory=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.factory=[0, 0, 0]                                                        #조합버튼이 따로 있음

    def findEmptyIndex(self):
        for i in range(9):
            if self.inventory[i] == 0:
                return i
        return -1 #빈칸없으면 -1반환

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
    
def addTower(inventoryNum, towerNum, towermaster, inventoryAndFactory):
    towermaster[towerNum].element=inventoryAndFactory.inventory[inventoryNum]
    inventoryAndFactory.inventory[inventoryNum]=0
