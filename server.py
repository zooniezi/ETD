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
import sys
import time

pg.init()

mine = pg.image.load("ElementIcon/alien (1).png")
sweeper = pg.image.load("sweeper.jpg")
towericon = pg.image.load("tower.png")
titleImg = pg.image.load("hungryTitle.png")
startImg = pg.image.load("startIcon.png")
quitImg = pg.image.load("quitIcon.png")
clickStartImg = pg.image.load("clickedStartIcon.png")
clickQuitImg = pg.image.load("clickedQuitIcon.png")


WIDTH = 1024
HEIGHT = 576
FPS = 60
CAPTION = "ETD"
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WINDOW = pg.display
WINDOW.set_caption(CAPTION)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))
CLOCK = pg.time.Clock()
THEFIRSTSTART = True

looptime = 0
#전역변수들
towerMaster = []
mobMaster = []
checkList=[[None, None],[None, None]]
inventoryAndFactory=storeinventory.InventoryAndFactory()
store=storeinventory.Store()

############################ 마우스 클릭 기능 구현 태규, 정수가 함 ㅅㄱ
"""
def isInInventory(coordinate):
    mousePosition = coordinate
    if mousePosition != [None, None]:
        if mousePosition[0] >=  779 and mousePosition[0] <=  (779+80*3) and mousePosition[1] >=  0 and mousePosition[1] <=  80*3:
            return True
        else:
            return False

def whatIsInventoryNum(coordinate):
    mousePosition = coordinate
    if mousePosition[0] >=  779 and mousePosition[0] <=  (779+80) and mousePosition[1] >=  0 and mousePosition[1] <=  80:
        return 0
    if mousePosition[0] >  859 and mousePosition[0] <=  (859+80) and mousePosition[1] >=  0 and mousePosition[1] <=  80:
        return 1
    if mousePosition[0] >  939 and mousePosition[0] <=  (939+80) and mousePosition[1] >=  0 and mousePosition[1] <=  80:
        return 2
    if mousePosition[0] >=  779 and mousePosition[0] <=  (779+80) and mousePosition[1] >  80 and mousePosition[1] <=  160:
        return 3
    if mousePosition[0] >  859 and mousePosition[0] <=  (859+80) and mousePosition[1] >  80 and mousePosition[1] <=  160:
        return 4
    if mousePosition[0] >  939 and mousePosition[0] <=  (939+80) and mousePosition[1] >  80 and mousePosition[1] <=  160:
        return 5
    if mousePosition[0] >=  779 and mousePosition[0] <=  (779+80) and mousePosition[1] >  160 and mousePosition[1] <=  240:
        return 6
    if mousePosition[0] >  859 and mousePosition[0] <=  (859+80) and mousePosition[1] >  160 and mousePosition[1] >=  240:
        return 7
    if mousePosition[0] >  939 and mousePosition[0] <=  (939+80) and mousePosition[1] >  160 and mousePosition[1] >=  240:
        return 8

def isInFactory(coordinate):
    mousePosition = coordinate
    if mousePosition != [None, None]:
        if mousePosition[0] >=  779 and mousePosition[0] <=  (779+60*4) and mousePosition[1] >= 250 and mousePosition[1] <= 310:
            return True
        else :
            return False

def whatIsFactoryNum(coordinate):
    mousePosition = coordinate
    if mousePosition[0] >=  779 and mousePosition[0] <=  (779+60) and mousePosition[1] >= 250 and mousePosition[1] <= 310:
        return 0
    if mousePosition[0] >  839 and mousePosition[0] <=  (839+60) and mousePosition[1] >= 250 and mousePosition[1] <= 310:
        return 1
    if mousePosition[0] >  899 and mousePosition[0] <=  (899+60) and mousePosition[1] >= 250 and mousePosition[1] <= 310:
        return 2
    if mousePosition[0] >  959 and mousePosition[0] <=  (959+60) and mousePosition[1] >= 250 and mousePosition[1] <= 310:
        return 3#조합 버튼
    # 리셋 버튼 추가 필요하고 일단은 리셋버튼 누르면 조합이 됨

def isInStore(coordinate):
    mousePosition = coordinate
    if mousePosition != [None, None]:
        if (mousePosition[0] >=  779 and mousePosition[0] <=  (779+60*3) and mousePosition[1] >= 320 and mousePosition[1] <= 380) or (mousePosition[0] >=  (779+60*3) and mousePosition[0] <=  (779+60*4) and mousePosition[1] > 350 and mousePosition[1] <= 380):
            return True
        else :
            return False

def whatIsStoreNum(coordinate):
    mousePosition = coordinate
    if mousePosition[0] >=  779 and mousePosition[0] <=  (779+60) and mousePosition[1] >= 320 and mousePosition[1] <= 380:
        return 0
    if mousePosition[0] >  839 and mousePosition[0] <=  (839+60) and mousePosition[1] >= 320 and mousePosition[1] <= 380:
        return 1
    if mousePosition[0] >  869 and mousePosition[0] <=  (869+60) and mousePosition[1] >= 320 and mousePosition[1] <= 380:
        return 2
    if mousePosition[0] >  929 and mousePosition[0] <=  (929+60) and mousePosition[1] > 350 and mousePosition[1] <= 380:
        return 3#이건 리롤 버튼

def isInTower(coordinate):
    mousePosition = coordinate
    for i in towerMaster:
        if mousePosition != [None, None]:
            if mousePosition[0] > i.towX and mousePosition[0] < i.towX + 50 and mousePosition[1] > i.towY and mousePosition[1] < i.towY + 50:
                return True
            else:
                return False

def whatIsTowerNum(coordinate):
    mousePosition = coordinate
    num = 0
    for i in towerMaster:
        if mousePosition[0] > i.towX and mousePosition[0] < i.towX + 50 and mousePosition[1] > i.towY and mousePosition[1] < i.towY + 50:
            return num
        num += 1    
    return num

def resetCheckList():
    checkList=[[None, None],[None, None]]

def playerAction():
    #일단 클릭 좌표가 checkList에 들어감
    if checkList[0]==[None, None]:
        checkList[0][0]=mousePosition()[0]
        checkList[0][1]=mousePosition()[1]
    else :
        checkList[1][0]=mousePosition()[0]
        checkList[1][1]=mousePosition()[1]

    #좌표에 따라서 경우의 수를 따져서 실행을 함
    #CheckList 두번째가 None일경우 if문이 False로 실행이 안됨.(조합버튼 제외)

    if isInInventory(checkList[0]):
        inventoryNum1=whatIsInventoryNum(checkList[0])
        if isInInventory(checkList[1]):
            #인벤토리 순서 바꾸기
            inventoryNum2=whatIsInventoryNum(checkList[1])
            inventoryAndFactory.inventory[inventoryNum1], inventoryAndFactory.inventory[inventoryNum2] = inventoryAndFactory.inventory[inventoryNum2], inventoryAndFactory.inventory[inventoryNum1]
            resetCheckList()
        elif isInFactory(checkList[1]):
            #인벤토리에서 팩토리 가기
            inventoryAndFactory.addFactory(inventoryNum1, whatIsFactoryNum(checkList[1]))
            resetCheckList()
        elif isInTower(checkList[1]):
            #인벤토리에서 타워로 이동
            inventoryAndFactory.addTower(inventoryNum1, whatIsTowerNum(checkList[1]), towerMaster, inventoryAndFactory)
            resetCheckList()

    if isInFactory(checkList[0]):
        factoryNum1=whatIsFactoryNum(checkList[0])
        #조합 버튼 누름
        if factoryNum1 == 3:
            if len(inventoryAndFactory.factory)==3 and inventoryAndFactory.factory[0].index== inventoryAndFactory.factory[1].index and inventoryAndFactory.factory[2].index == inventoryAndFactory.factory[1].index :
                inventoryAndFactory.compoundLevelUp()#믹스도 넣어야함 나중에
                resetCheckList()
        else:
            if isInInventory(checkList[1]):
                #팩토리에서 인벤토리로 이동
                inventoryNum2=whatIsInventoryNum(checkList[1])
                inventoryAndFactory.addInventory(inventoryNum2, factoryNum1)             
                resetCheckList()
            elif isInFactory(checkList[1]):
                #팩토리에서 순서 바꾸기
                factoryNum2=whatIsFactoryNum(checkList[1])
                if factoryNum2 != 3:
                    inventoryAndFactory.factory[factoryNum1], inventoryAndFactory.inventory[factoryNum2] = inventoryAndFactory.inventory[factoryNum2], inventoryAndFactory.inventory[factoryNum1]
                    resetCheckList()
                #두번째 클릭으로 조합 버튼 누름
                elif factoryNum2 == 3 and len(inventoryAndFactory.factory)==3 and inventoryAndFactory.factory[0].index== inventoryAndFactory.factory[1].index and inventoryAndFactory.factory[2].index == inventoryAndFactory.factory[1].index :
                    inventoryAndFactory.compoundLevelUp()#믹스도 넣어야함 나중에
                    resetCheckList()
            elif isInTower(checkList[1]):
                #팩토리에서 타워로 이동
                #나중에 추가
                resetCheckList()
    if isInStore(checkList[0]) or isInStore(checkList[1]):
        if checkList[1]==[None, None]:
            storeNum=whatIsStoreNum(checkList[0])
        else:
            storeNum=whatIsStoreNum(checkList[1])
        if whatIsStoreNum != 3:
            store.buy(store.shelf[storeNum])
        else:
            inventoryAndFactory.reroll(gold.playerGold)
    if isInTower(checkList[0]):
        towerNum1 = whatIsTowerNum(checkList[0])
        if towerMaster[towerNum1].element.price == 0:
            resetCheckList()
        elif isInInventory(checkList[1]):
            #타워에서 인벤토리로 이동
            inventoryNum2 = whatIsInventoryNum(checkList[1])
            inventoryAndFactory.inventory[inventoryNum2] = towerMaster[towerNum1].element
            towerMaster[towerNum1].element = storeinventory.element.Empty()
            resetCheckList()
        elif isInFactory(checkList[1]):
            #타워에서 팩토리로 이동
            #나중에 업데이트
            resetCheckList()
        elif isInTower(checkList[1]):
            #타워끼리 순서 바꾸기
            towerNum2 = whatIsTowerNum(checkList[1])
            towerMaster[towerNum1].element, towerMaster[towerNum2].element = towerMaster[towerNum2].element, towerMaster[towerNum1].element
            resetCheckList()
"""

############################# 버튼 클래스 준학이가 함 ㅈㅅ
class Button:
    def __init__(self, img, x, y, width, height, imgAct, xAct, yAct, action1 = None, action2 = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            SCREEN.blit(imgAct,(xAct, yAct))
            if click[0] and action1 != None:
                time.sleep(1)
                action2()   
                action1()
        else:
            SCREEN.blit(img,(x,y))


###  zzzzz
def quitGame():
    pg.quit()
    sys.exit()

def mainMenu():

    menu = True

    while menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        SCREEN.fill(WHITE)
        
        titletext = SCREEN.blit(titleImg, (220,150))
        startButton = Button(startImg,280,260,60,20,clickStartImg,273,258,gameStart,roundStart)
        quitButton = Button(quitImg,445,260,60,20,clickQuitImg,440,258,quitGame,None)
        pg.display.update()

## roundStart 버튼 누르면 round 시작되고, 시간 다 리셋하는 느낌
def roundStart():
    global roundNumber, start_ticks, population
    roundNumber += 1
    population = (roundNumber+4)*10 + 1 #라운드에 출현하는 mob의 수   
    roundGenerator()
    start_ticks = pygame.time.get_ticks()
    mob.atk_time = datetime.now()

## round를 생성함
def roundGenerator():
    global population, mobMaster
    # 몹마스터에 몹객체 생성 
    # 1라운드: 1티어 몹 50마리, 2라운드: 2티어 몹 60마리, 3라운드: 3티어 몹 70마리
    # index 1 = 1번 몹, index 50 = 50번째 몹
    mobMaster = []
    for i in range(1, population): 
        mobMaster.append(mob.Minion(tierList[roundNumber], i)) 
    # 몹마스터에 보스객체 생성, 보스티어는 현재 라운드 + 5티어
    mobMaster.append(mob.Boss(tierList[roundNumber+5],population))


#라운드 넘버(전역변수)
roundNumber = 0
population = 0 












#몹 티어리스트
tierList = [["hp,armor,speed,dropGold,dropElement,damage,image"],
[100,10,2,2,0,5,mine],
[150,15,2,2,0,5,mine],
[200,20,3,5,0,5,mine],
[250,25,3,5,0,5,mine],
[300,30,3,5,0,5,mine],
[1000,19,2,20,"elt",20,sweeper],
[1500,60,2,30,"elt",20,sweeper],
[2000,70,2,40,"elt",20,sweeper],
[2500,80,2,50,"elt",20,sweeper],
[5000,100,3,9999,0,100]]

gameFont = pygame.font.Font(None, 40)


def setTowerCoordinate(towerCoordinate):
    coordinate = []
    for i in towerCoordinate:
        setTowerCoordinate = random.sample(i,1)
        coordinate.append(setTowerCoordinate[0])
    return coordinate

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
        if i.element != None:
            SCREEN.blit(pg.image.load(i.element.image),(i.towX+10, i.towY-20))
        SCREEN.blit(towericon,(i.towX,i.towY))
        

#가능한 타워 좌표 리스트
availableTowerCoordinate = [
[(100,0),(100,50),(100,100),(100,150),(100,200),
(150,200),(200,200),(250,200),(300,200),(350,200),(400,200),(450,200),(500,200),(550,200),(600,200)],
[(600,250),(600,300),(600,350),
(550,350),(500,350),(450,350),(400,350),(350,350),(300,350),(250,350),(200,350),(150,350),(100,350)],
[(100,400),(100,450),(100,500),
(200,0),(200,50),(200,100)],
[(250,100),(300,100),(350,100),(400,100),(450,100),(500,100),(550,100),(600,100),(650,100),(700,100)],
[(700,150),(700,200),(700,250),(700,300),(700,350),(700,400),(700,450)],
[(650,450),(600,450),(550,450),(500,450),(450,450),(400,450),(350,450),(300,450),(250,450),(200,450),
(200,500)]]

def renderInventory():
    for j in range (3):
        for i in range (3):
            pygame.draw.rect(SCREEN,BLACK,(779+80*i,0+j*80,80,80),1)
            if inventoryAndFactory.inventory[j*3+i] != 0:
                SCREEN.blit(pg.image.load(inventoryAndFactory.inventory[j*3+i].image), (804+(80*i), 25+(80*j)))  
        

def renderFactory():
    for i in range (4):
        pygame.draw.rect(SCREEN,BLACK,(779+60*i,250,60,60),1)
        if i != 3:
            if inventoryAndFactory.factory[i] != 0:
                SCREEN.blit(pg.image.load(inventoryAndFactory.factory[i].image), (794+(60*i), 265))

def renderStore():
    for i in range (3):
        pygame.draw.rect(SCREEN,BLACK,(779+60*i,320,60,60),1)
        if store.shelf[i] != 0:
            SCREEN.blit(pg.image.load(store.shelf[i].image), (794+(60*i), 335))
    for i in range (2):
        pygame.draw.rect(SCREEN,BLACK,(959,320+30*i,60,30),1)

def renderDictionary():
    pygame.draw.rect(SCREEN,BLACK,(779,400,120,160),1)

def renderStartButton():
    pygame.draw.rect(SCREEN,BLACK,(899,400,120,160),1)

def renderPlayerHp():
    playerLeftHp = gameFont.render("HP: {}".format(mob.playerHp), True, (255,255,255))
    SCREEN.blit(playerLeftHp, (400,100))

def renderPlayerGold():
    playerLeftGold = gameFont.render("GOLD: {}".format(gold.playerGold.playerGold), True, (255,255,255))
    SCREEN.blit(playerLeftGold, (499,200))
        



#라운드에 1초마다 몹을 생성
def mobStart():
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


# 시계 표현용 시간 정보
totalTime = 90



#게임 맵 구동및 준비 과정
towerCoordinate = setTowerCoordinate(availableTowerCoordinate)
for i in range(6):
    if i < 4:
        towerMaster.append(tower.Tower(towerCoordinate[i][0], towerCoordinate[i][1], storeinventory.element.Fire()))
    else:
        towerMaster.append(tower.Tower(towerCoordinate[i][0], towerCoordinate[i][1], storeinventory.element.Water()))
"""원본함수(공격속도 루프단위 계산임, 이제 안쓸듯함)
def towerAttack(tm):
    for thisTower in tm:
        tarMob = thisTower.targeting(mobMaster)
        if tarMob != None and thisTower.element.attackSpeed - thisTower.attackCounter <= 0:
            thisTower.element.damageDealt(tarMob)
            #타워 공격시 타워와 대상 몹 사이에 레이저(선) 렌더링
            pg.draw.line(SCREEN, RED, [thisTower.towX+25, thisTower.towY], [tarMob.x+15, tarMob.y+15], 15)
            thisTower.attackCounter = 0
        else:
            thisTower.attackCounter += 1
"""
#타워 타겟팅 및 공격속도에 맞게 타겟팅 대상 공격(레이저 그려짐)
def towerAttack(tm):
    for thisTower in tm:
        global THEFIRSTSTART
        tarMob = thisTower.targeting(mobMaster)
        if THEFIRSTSTART:   #최초 공격(딜레이없이)
            if tarMob != None:
                thisTower.element.damageDealt(tarMob)
                thisTower.element.attackCounter = thisTower.element.attackSpeed
                #타워 공격시 타워와 대상 몹 사이에 레이저(선) 렌더링
                pg.draw.line(SCREEN, thisTower.element.attackColor, [thisTower.towX+25, thisTower.towY], [tarMob.x+15, tarMob.y+15], 15)
                THEFIRSTSTART = False
                print("first attack done")

        thisTower.element.attackCounter -= looptime
        
        if tarMob != None and thisTower.element.attackCounter < 0:
            thisTower.element.damageDealt(tarMob)
            thisTower.element.attackCounter = thisTower.element.attackSpeed
            #타워 공격시 타워와 대상 몹 사이에 레이저(선) 렌더링
            pg.draw.line(SCREEN, thisTower.element.attackColor, [thisTower.towX+25, thisTower.towY], [tarMob.x+15, tarMob.y+15], 15)
        elif tarMob == None:
            thisTower.attackCounter = thisTower.element.attackSpeed

#타워 사거리 렌더링
def towerRangeRender(tm):
    for thisTower in tm:
        pg.draw.circle(SCREEN, CYAN, [thisTower.towX+25, thisTower.towY+25], thisTower.attackRange, 2)


#실행부
def gameStart():
    global looptime
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
        #태규 정수
#        if LMBDown(event):
#           playerAction()

        looptime = CLOCK.get_time()
        SCREEN.fill(BLACK)
        towerRender()
        towerRangeRender(towerMaster)
        pg.draw.rect(SCREEN, WHITE, [774, 0, 300, 576])
        renderInventory()
        renderFactory()
        renderStore()
        renderDictionary()
        renderStartButton()
        renderPlayerHp()
        renderPlayerGold()
        CLOCK.tick(FPS)
        #몹 생성&몹 랜더링
        mobStart()
        mobSpawn()
        

        startButton = Button(startImg,899,400,60,20,clickStartImg,895,398,gameStart,roundStart)

        #남은 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        #타이머
        timer = gameFont.render("time: " + str(int(totalTime-elapsed_time)), True, (255,255,255))
        roundNumberText = gameFont.render("ROUND : {}".format(roundNumber),True,WHITE)
        populationText = gameFont.render("POPULATION : {}".format(population),True,WHITE)

        towerAttack(towerMaster)


        #타이머 랜더링
        SCREEN.blit(timer, (240, 10))
        SCREEN.blit(roundNumberText,(500,30))
        SCREEN.blit(populationText,(300,60))
        pg.display.update()

mainMenu()
