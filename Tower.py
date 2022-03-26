from cmath import sqrt
import math

class Tower:
    
    def __init__(self,x,y,element):
        self.attackRange = element.attackRange
        self.towX = x
        self.towY = y
        self.hasElement = False
        self.element = element

    def targeting(self,mobMaster):# mobMaster: 라운드의 모든 몬스터 받아오기
        targetMob = None
        for i in mobMaster:
            if i.alive == False:
                continue

            if math.sqrt((i.x-self.towX)**2 + (i.y-self.towY)**2) <= self.attackRange:
                targetMob = i
                break
            
        return targetMob



#################################

# tow = Tower(1,1,None)

# class mob:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.alive = True

    

# mob1 = mob(1,2)
# mob2 = mob(2,2)
# mob3 = mob(6,1)
# mob4 = mob(3,4)
# mobMaster = [mob1,mob2,mob3,mob4]

# target = tow.targeting(mobMaster)
# print(target.x)