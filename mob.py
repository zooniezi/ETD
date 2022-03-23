from re import I
import pygame
import pygame as pg
from datetime import timedelta
from datetime import datetime

pygame.init()

mine = pg.image.load("mine.png")
sweeper = pg.image.load("sweeper.jpg")

WIDTH = 1024
HEIGHT = 576
FPS = 60
CAPTION = "ETD"
CYAN    = (0, 255, 255)
BLACK   = (0, 0, 0)

WINDOW = pg.display
WINDOW.set_caption(CAPTION)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))

gameFont = pygame.font.Font(None, 40)


tierList = [["hp,armor,speed,dropGold,dropElement,damage,image"],[100,10,2,2,0,5,mine],[150,15,2,2,0,5,mine],[200,20,3,5,0,5,mine],[250,25,3,5,0,5],[300,30,3,5,0,5],[1000,50,2,20,"elt",20,sweeper],[1500,60,2,30,"elt",20],[2000,70,2,40,"elt",20],[2500,80,2,50,"elt",20],[5000,100,3,9999,0,100]]

#시간 이용을 위한 설정

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
        if self.onMap == True:

            # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용

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
        elif self.onMap == False:
            pass


    #몹의 hp가 0 이하가 되었을 때 맵에서 삭제, 플레이어 골드량에 해당 골드 추가
    def die(self):
        global gold
        if self.tier[0] <= 0 and self.alive == True:
            self.alive = False
            self.onMap = False
            gold += self.tier[3]

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
    

#라운드에 1초마다 몹을 생성
def start():
        global atk_time
        for i in range(1,population+1):
            if timedelta(seconds = i-1) <= datetime.now() - atk_time:
                mobMaster[i-1].onMap = True

        
# 몹 랜더링
def spawn():
    cnt = 1
    for i in mobMaster:
        if i.onMap == True and cnt<=population:
            SCREEN.blit(i.image,(i.x,i.y))
            leftHp = gameFont.render("{}".format(i.hp),True,CYAN)
            SCREEN.blit(leftHp,(i.x-5,i.y+20))
            cnt += 1
        if i.onMap == True and cnt>population:
            SCREEN.blit(i.image,(i.x,i.y))
            leftHp = gameFont.render("{}".format(i.hp),True,CYAN)
            SCREEN.blit(leftHp,(i.x-5,i.y+20))

roundNumber =1
population = (roundNumber+4)*10 + 1 #라운드에 출현하는 mob의 수

        
# 몹마스터에 몹객체 생성 
# 1라운드: 1티어 몹 50마리, 2라운드: 2티어 몹 60마리, 3라운드: 3티어 몹 70마리
# index 1 = 1번 몹, index 50 = 50번째 몹
mobMaster = []
for i in range(1, population): 
    mobMaster.append(Minion(tierList[roundNumber], i)) 

# 몹마스터에 보스객체 생성, 보스티어는 현재 라운드 + 5티어
mobMaster.append(Boss(tierList[roundNumber+5],population))

atk_time = datetime.now()
playerHp = 100
gold = 10
print(playerHp)

# 시간 정보
totalTime = 60
start_ticks = pygame.time.get_ticks()

