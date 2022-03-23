from re import I
import pygame
import pygame as pg
from datetime import timedelta
from datetime import datetime
import random
from time import sleep
import threading
#import module files
import mob
import gold
import storeinventory
import tower

pg.init()

mine = pg.image.load("mine.png")
sweeper = pg.image.load("sweeper.jpg")
towericon = pg.image.load("tower.png")

WIDTH = 1024
HEIGHT = 576
FPS = 60
CAPTION = "ETD"
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW = pg.display
WINDOW.set_caption(CAPTION)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))

#전역변수들
towerMaster = []
mobMaster = []
playerGold = gold.Gold()
#라운드 넘버(전역변수)
roundNumber =1
population = (roundNumber+4)*10 + 1 #라운드에 출현하는 mob의 수
#가능한 타워 좌표 리스트
availableTowerCoordinate = [
(100,0),(100,50),(100,100),(100,150),(100,200),
(150,200),(200,200),(250,200),(300,200),(350,200),(400,200),(450,200),(500,200),(550,200),(600,200),
(600,250),(600,300),(600,350),
(550,350),(500,350),(450,350),(400,350),(350,350),(300,350),(250,350),(200,350),(150,350),(100,350),
(100,400),(100,450),(100,500),
(200,0),(200,50),(200,100),
(250,100),(300,100),(350,100),(400,100),(450,100),(500,100),(550,100),(600,100),(650,100),(700,100),
(700,150),(700,200),(700,250),(700,300),(700,350),(700,400),(700,450),
(650,450),(600,450),(550,450),(500,450),(450,450),(400,450),(350,450),(300,450),(250,450),(200,450),
(200,500)]

INVENTORYANDFACRTORY=storeinventory.InventoryAndFactory()
STORE=storeinventory.Store()

#몹 티어리스트
tierList = [["hp,armor,speed,dropGold,dropElement,damage,image"],[100,10,2,2,0,5,mine],[150,15,2,2,0,5,mine],[200,20,3,5,0,5,mine],[250,25,3,5,0,5],[300,30,3,5,0,5],[1000,19,2,20,"elt",20,sweeper],[1500,60,2,30,"elt",20],[2000,70,2,40,"elt",20],[2500,80,2,50,"elt",20],[5000,100,3,9999,0,100]]


gameFont = pygame.font.Font(None, 40)


def setTowerCoordinate(towerCoordinate, numOfTower):
    coordinate = random.sample(towerCoordinate, numOfTower)
    return coordinate


#라운드에 1초마다 몹을 생성
def mobStart():
        # global mob.atk_time
        for i in range(1,population+1):
            if timedelta(seconds = i-1) <= datetime.now() - mob.atk_time:
                mobMaster[i-1].onMap = True
                mobMaster[i-1].move()
# 몹 랜더링
def mobSpawn():
    for i in mobMaster:
        if i.onMap == True and i.alive == True:
            SCREEN.blit(i.image,(i.x,i.y))
            leftHp = gameFont.render("{}".format(i.hp),True,CYAN)
            SCREEN.blit(leftHp,(i.x-5,i.y+20))


def LMBDown(event):
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        return True
    return False

def LMBUp(event):
    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
        return True
    return False

def mousePosition():
    return pg.mouse.get_pos()

#타워 렌더링
def towerRender():
    for i in towerMaster:
        SCREEN.blit(towericon,(i.towX,i.towY))

def renderInventory():
    for j in range (3):
        for i in range (3):
            pygame.draw.rect(SCREEN,BLACK,(779+80*i,0+j*80,80,80),1)

def renderFactory():
    for i in range (4):
        pygame.draw.rect(SCREEN,BLACK,(779+60*i,250,60,60),1)

def renderStore():
    for i in range (3):
        pygame.draw.rect(SCREEN,BLACK,(779+60*i,320,60,60),1)
    for i in range (2):
        pygame.draw.rect(SCREEN,BLACK,(959,320+30*i,60,30),1)

def renderDictionary():
    pygame.draw.rect(SCREEN,BLACK,(779,400,120,160),1)

def renderStart():
    pygame.draw.rect(SCREEN,BLACK,(899,400,120,160),1)

        
# 몹마스터에 몹객체 생성 
# 1라운드: 1티어 몹 50마리, 2라운드: 2티어 몹 60마리, 3라운드: 3티어 몹 70마리
# index 1 = 1번 몹, index 50 = 50번째 몹
for i in range(1, population): 
    mobMaster.append(mob.Minion(tierList[roundNumber], i)) 

# 몹마스터에 보스객체 생성, 보스티어는 현재 라운드 + 5티어
mobMaster.append(mob.Boss(tierList[roundNumber+5],population))


# 시계 표현용 시간 정보
totalTime = 90
start_ticks = pygame.time.get_ticks()

#게임 맵 구동및 준비 과정

towerCoordinate = setTowerCoordinate(availableTowerCoordinate,6)
for i in range(6):
    towerMaster.append(tower.Tower(towerCoordinate[i][0], towerCoordinate[i][1], storeinventory.element.Fire()))

def towerAttack(tm):
    for thisTower in tm:
        tarMob = thisTower.targeting(mobMaster)
        if tarMob != None and thisTower.element.attackSpeed - thisTower.attackCounter <= 0:
            thisTower.element.damageDealt(tarMob)
            thisTower.attackCounter = 0
        else:
            thisTower.attackCounter += 1
#실행부
running = True
while running:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False

    SCREEN.fill(BLACK)
    towerRender()
    pg.draw.rect(SCREEN, WHITE, [774, 0, 300, 576])
    renderInventory()
    renderFactory()
    renderStore()
    renderDictionary()
    renderStart()
    pg.time.Clock().tick(FPS)

    #몹 생성&몹 랜더링
    mobStart()
    mobSpawn()
    towerAttack(towerMaster)
    #남은 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    #타이머
    timer = gameFont.render("time: " + str(int(totalTime-elapsed_time)), True, (255,255,255))

    #타이머 랜더링
    SCREEN.blit(timer, (240, 10))

    pg.display.update()


