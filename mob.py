#몹이 경로 끝을 나갔을 때의 시간
from gold import Gold
from datetime import timedelta
from datetime import datetime
playerHp = 100
atk_time = datetime.now()
aa_time = datetime.now()

#몹 티어리스트

class Mob:
    def __init__(self,tier,index):
        self.tier = tier
        self.hp = self.tier[0]
        self.armor = self.tier[1]
        self.speed = self.tier[2]
        self.dropGold = self.tier[3]
        self.dropElement = self.tier[4]
        self.damage = self.tier[5]
        self.image = self.tier[6]
        self.index = index
        self.alive = True
        self.onMap = False
        self.x = 150
        self.y = 540

    #몹을 움직임 경로 & 몹 등장
    def move(self):
        if self.onMap == True and self.alive == True:

            # 이미지의 좌표값을 이용해 이동
            if self.y >= 400:
                self.y -= self.speed

            elif self.y <= 400 and self.y > 150 and self.x <= 650:
                self.x += self.speed
                
            elif self.y <= 400 and self.y >= 150 and self.x >= 650:
                self.y -= self.speed

            elif self.y <= 150 and self.x >= 150:
                self.x -= self.speed

            elif self.y < 150 and self.x < 150:
                self.y -= self.speed

            self.attack()
            self.die()

        #mob이 죽거나 경로 끝까지 이동했을 경우 움직임을 멈추고 동시에 사라짐
        elif self.onMap == False and self.alive == False:
            pass

    #몹의 hp가 0 이하가 되었을 때 맵에서 삭제, 플레이어 골드량에 해당 골드 추가
    def die(self):
        #global playergold
        if self.hp <= 0 and self.alive == True:
            self.alive = False
            self.onMap = False
            #playergold.playerGold += self.tier[3]
            print(self.alive)
            del(self)
            

    #몹이 경로 끝까지 이동했을 때 플레이어에게 데미지 구현, 맵에서 삭제
    def attack(self):
        global playerHp
        if self.y <= 0 and self.alive == True:
            playerHp -= self.tier[5]
            self.alive = False
            self.onMap = False
            print(playerHp)

class Minion(Mob):
    def __init__(self,tier,index):
        super().__init__(tier,index)

class Boss(Mob):
    def __init__(self,tier,index):
        super().__init__(tier,index)